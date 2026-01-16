import random
from .forms import PasswordChangeWithCodeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Importación de modelos
from LaboratorioMinozzi.models import EstudiosDisponibles, Pacientes, ResultadosdeEstudios, Perfil

# Importación de formularios (asegúrate de que todos existan en forms.py)
from .forms import (
    PacienteForm, 
    EstudioForm, 
    historiaClinicaForm, 
    RegistroUsuarioForm, 
    ResultadoEstudioForm,
    PerfilForm,
    UserEditForm,
    PasswordChangeWithCodeForm  # Agregado
)

# --- VISTAS GENERALES ---

def home(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/index.html")

def about(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/about.html")

# --- VISTAS DE PACIENTES ---

class PacienteListView(LoginRequiredMixin, ListView):
    model = Pacientes
    template_name = 'LaboratoriodeAnalisisClinicosMinozzi/lista_pacientes.html'
    context_object_name = 'pacientes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        dni = self.request.GET.get('dni')
        if dni:
            queryset = queryset.filter(DNI__icontains=dni)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PacienteForm()
        return context

class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Pacientes
    template_name = "LaboratoriodeAnalisisClinicosMinozzi/detalle_paciente.html"
    context_object_name = "paciente"
    pk_url_kwarg = 'paciente_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resultados'] = ResultadosdeEstudios.objects.filter(
            paciente=self.object
        ).prefetch_related('estudio').order_by('-fecha_estudio')
        return context

@login_required
def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Paciente registrado con éxito.")
    return redirect('lista_pacientes')

# --- VISTAS DE ESTUDIOS Y RESULTADOS ---

@login_required
def subir_resultado(request):
    dni_buscado = request.GET.get('dni_paciente')
    nombre_buscado = request.GET.get('nombre_paciente')
    paciente_encontrado = None
    
    if dni_buscado:
        paciente_encontrado = Pacientes.objects.filter(DNI=dni_buscado).first()
    elif nombre_buscado:
        paciente_encontrado = Pacientes.objects.filter(apellido__icontains=nombre_buscado).first()

    if request.method == "POST":
        form = ResultadoEstudioForm(request.POST, request.FILES)
        if form.is_valid():
            instancia = form.save()
            
            if instancia.paciente.email:
                try:
                    subject = "Resultado Disponible - Laboratorio Minozzi"
                    body = f"Hola {instancia.paciente.nombre}, su resultado ya está disponible."
                    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [instancia.paciente.email])
                    email.attach_file(instancia.resultado.path)
                    email.send()
                    messages.success(request, "Resultado cargado y enviado por mail.")
                except Exception:
                    messages.warning(request, "Resultado guardado pero no se pudo enviar el email.")
            else:
                messages.success(request, "Protocolo cargado con éxito.")
            return redirect('home')
    else:
        initial_data = {'paciente': paciente_encontrado} if paciente_encontrado else {}
        form = ResultadoEstudioForm(initial=initial_data)

    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html", {
        "form": form,
        "paciente_encontrado": paciente_encontrado
    })

def lista_estudios(request):
    estudios = EstudiosDisponibles.objects.all()
    form = EstudioForm()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_estudios.html", {
        "estudios": estudios, "form": form
    })

@login_required
def registrar_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudio agregado al catálogo.")
    return redirect('lista_estudios')

# --- VISTAS DE USUARIO Y PERFIL ---

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenido/a {user.username}.")
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'LaboratoriodeAnalisisClinicosMinozzi/registro.html', {'form': form})

@login_required
def profile_detail(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/profile_detail.html", {"user": request.user})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "¡Perfil actualizado con éxito!")
            return redirect('profile_detail')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)
    
    return render(request, 'LaboratoriodeAnalisisClinicosMinozzi/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

# --- SEGURIDAD AVANZADA (CAMBIO DE PASSWORD CON MAIL) ---

@login_required
def cambiar_password_seguro(request):
    # Generar código si no existe en la sesión
    if 'codigo_seguridad' not in request.session:
        codigo = str(random.randint(100000, 999999))
        request.session['codigo_seguridad'] = codigo
        
        try:
            send_mail(
                'Código de seguridad - Laboratorio Minozzi',
                f'Hola {request.user.username}, tu código para cambiar la contraseña es: {codigo}',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.info(request, "Se ha enviado un código de verificación a tu correo.")
        except Exception:
            messages.error(request, "No se pudo enviar el código por mail. Revisa tu configuración de correo.")

    if request.method == 'POST':
        form = PasswordChangeWithCodeForm(request.user, request.POST)
        codigo_ingresado = request.POST.get('codigo_verificacion')
        
        if form.is_valid():
            if codigo_ingresado == request.session.get('codigo_seguridad'):
                user = form.save()
                update_session_auth_hash(request, user)
                del request.session['codigo_seguridad']
                messages.success(request, '¡Contraseña actualizada con éxito!')
                return redirect('profile_detail')
            else:
                messages.error(request, 'El código de verificación es incorrecto.')
    else:
        form = PasswordChangeWithCodeForm(request.user)
    
    return render(request, 'registration/password_change_form.html', {'form': form})

# Busca esta parte en tu views.py o agrégala si falta:

@login_required
def historia_clinica(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        form = historiaClinicaForm(request.POST) # Aquí usas el FORMULARIO
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada de historial guardada.")
            return redirect('historia_clinica')
    else:
        form = historiaClinicaForm()
    
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/historia_clinica.html", {
        'pacientes': pacientes,
        'form': form
    })
# --- VISTAS DE EDICIÓN Y BORRADO (CORREGIDAS) ---

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Pacientes
    # Usamos los mismos campos que en tu modelo
    fields = ['nombre', 'apellido', 'dni', 'email', 'fecha_nacimiento', 'foto']
    # Corregimos la ruta para que coincida con tu carpeta larga
    template_name = 'LaboratoriodeAnalisisClinicosMinozzi/paciente_form.html'
    # Corregimos el nombre del redirect para que coincida con tu urls.py
    success_url = reverse_lazy('lista_pacientes') 

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Pacientes
    # Corregimos la ruta para que coincida con tu carpeta larga
    template_name = 'LaboratoriodeAnalisisClinicosMinozzi/paciente_confirm_delete.html'
    # Corregimos el nombre del redirect para que coincida con tu urls.py
    success_url = reverse_lazy('lista_pacientes')