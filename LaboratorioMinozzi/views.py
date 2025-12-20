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