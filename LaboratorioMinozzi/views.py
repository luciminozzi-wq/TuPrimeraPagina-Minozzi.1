from django.shortcuts import render
from LaboratorioMinozzi.models import EstudiosDisponibles, Pacientes, ResultadosdeEstudios

def home(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/index.html")


def lista_estudios(request):
    estudios = EstudiosDisponibles.objects.all()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_estudios.html", {"estudios": estudios})


def subir_resultado(request):
    if request.method == "POST":
        paciente_id = request.POST.get("paciente")
        estudio_id = request.POST.get("estudio_id")
        fecha_estudio = request.POST.get("fecha_estudio")
        resultado_file = request.FILES.get("resultado_file")
        bioquimico_responsable = request.POST.get("bioquimico_responsable")

        paciente = Pacientes.objects.get(id=paciente_id)
        estudio = EstudiosDisponibles.objects.get(id=estudio_id)

        nuevo_resultado = ResultadosdeEstudios(
            paciente=paciente,
            estudio=estudio,
            fecha_estudio=fecha_estudio,
            resultado=resultado_file,
            bioquimico_responsable=bioquimico_responsable
        )
        nuevo_resultado.save()
        return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado_exito.html")

    estudios = EstudiosDisponibles.objects.all()
    pacientes = Pacientes.objects.all()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html", {"estudios": estudios, "pacientes": pacientes})


def detalle_paciente(request, paciente_id):
    paciente = Pacientes.objects.get(id=paciente_id)
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/detalle_paciente.html", {"paciente": paciente})

from django.shortcuts import render, redirect
from .models import Pacientes, EstudiosDisponibles

def home(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/index.html")

def lista_pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_pacientes.html", {'pacientes': pacientes})

def lista_estudios(request):
    estudios = EstudiosDisponibles.objects.all()
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_estudios.html", {'estudios': estudios})

from django.shortcuts import render, redirect
from django.contrib import messages # Para mostrar avisos de éxito o error
from .models import Pacientes

def registrar_paciente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('DNI')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_nac = request.POST.get('fecha_nacimiento')

        try:
            nuevo_paciente = Pacientes.objects.create(
                nombre=nombre,
                apellido=apellido,
                DNI=dni,
                email=email,
                telefono=telefono,
                fecha_nacimiento=fecha_nac
            )
            messages.success(request, f"Paciente {apellido} registrado con éxito.")
        except Exception as e:
            messages.error(request, f"Error al registrar: {e}")
        
        return redirect('lista_pacientes')
    
    return redirect('lista_pacientes')

def historia_clinica(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/lista_pacientes.html")

def subir_resultado(request):
    return render(request, "LaboratoriodeAnalisisClinicosMinozzi/subir_resultado.html")