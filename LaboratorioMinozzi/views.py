# LaboratorioMinozzi/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
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

def lista_pacientes(request):
    dni_buscado = request.GET.get('dni')
    if dni_buscado:
        pacientes = Pacientes.objects.filter(DNI__icontains=dni_buscado)
    else:
        pacientes = Pacientes.objects.all()
    
    form = PacienteForm()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_pacientes.html", {
        'pacientes': pacientes, 
        'form': form
    })

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Paciente registrado con éxito.")
    return redirect('lista_pacientes')

def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Pacientes, id=paciente_id)
    resultados = ResultadosdeEstudios.objects.filter(paciente=paciente).prefetch_related('estudio').order_by('-fecha_estudio')
    
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/detalle_paciente.html", {
        "paciente": paciente,
        "resultados": resultados
    })

def lista_estudios(request):
    estudios = EstudiosDisponibles.objects.all()
    form = EstudioForm()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_estudios.html", {
        "estudios": estudios,
        "form": form
    })

def registrar_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudio agregado al catálogo.")
    return redirect('lista_estudios')

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
            messages.success(request, "Protocolo cargado con éxito.")
            return redirect('home')
        else:
            print(form.errors) 
    else:
        initial_data = {}
        if paciente_encontrado:
            initial_data['paciente'] = paciente_encontrado
        form = ResultadoEstudioForm(initial=initial_data)

    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html", {
        "form": form,
        "paciente_encontrado": paciente_encontrado
    })
    
    if dni_buscado:
        paciente_encontrado = Pacientes.objects.filter(DNI=dni_buscado).first()
    elif nombre_buscado:
        paciente_encontrado = Pacientes.objects.filter(apellido__icontains=nombre_buscado).first()

    if request.method == "POST":
        form = ResultadoEstudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Protocolo cargado con éxito.")
            return redirect('home')
        else:
            print(form.errors) 
    else:
        initial_data = {}
        if paciente_encontrado:
            initial_data['paciente'] = paciente_encontrado
        form = ResultadoEstudioForm(initial=initial_data)

    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html", {
        "form": form,
        "paciente_encontrado": paciente_encontrado
    })

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

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenido/a {user.username}. Cuenta de personal creada.")
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Error en el registro. Verifique los requisitos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'LaboratoriodeAnalisisClinicosMinozzi/registro.html', {'form': form})

@login_required
def profile_detail(request):
    return render(request, "users/profile_detail.html", {"user": request.user})
