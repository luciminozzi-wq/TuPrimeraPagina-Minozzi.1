from django.contrib import admin
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios

@admin.register(Pacientes)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'DNI', 'email')
    search_fields = ('apellido', 'DNI')

@admin.register(EstudiosDisponibles)
class EstudioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

@admin.register(ResultadosdeEstudios)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'estudio', 'fecha_estudio', 'bioquimico_responsable')
