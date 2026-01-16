from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView # Importamos DetailView para cumplir requisito de 2 CBV
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import PerfilForm
from LaboratorioMinozzi.models import EstudiosDisponibles, Pacientes, ResultadosdeEstudios
from .forms import (
    PacienteForm, 
    EstudioForm, 
    historiaClinicaForm, 
    RegistroUsuarioForm, 
    ResultadoEstudioForm
)

def home(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/index.html")

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
        # Traemos los resultados filtrados por el paciente actual
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
                except:
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
    return render(request, "users/profile_detail.html", {"user": request.user})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('profile_detail')
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'users/editar_perfil.html', {'form': form})
@login_required
def historia_clinica(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        form = historiaClinicaForm(request.POST)
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