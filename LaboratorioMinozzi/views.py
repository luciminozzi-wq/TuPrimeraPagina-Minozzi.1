from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from LaboratorioMinozzi.models import EstudiosDisponibles, Pacientes, ResultadosdeEstudios

# Importación de formularios
# Ajusta '.forms' si tu archivo de formularios tiene otro nombre
from .forms import (
    PacienteForm, 
    EstudioForm, 
    ResultadoForm, 
    historiaClinicaForm
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
    return redirect('lista_pacientes')

def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Pacientes, id=paciente_id)
    resultados = ResultadosdeEstudios.objects.filter(paciente=paciente)
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
    if request.method == "POST":
        form = ResultadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado_exito.html")
    else:
        form = ResultadoForm()
    
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html", {"form": form})

def historia_clinica(request):
    pacientes = Pacientes.objects.all()
    if request.method == 'POST':
        form = historiaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Paciente guardado con éxito.")
            return redirect('historia_clinica')
    else:
        form = historiaClinicaForm()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/historia_clinica.html", {
        'pacientes': pacientes,
        'form': form
    })