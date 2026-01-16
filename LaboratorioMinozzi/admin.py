from django.contrib import admin
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios
from .models import ResultadosdeEstudios

@admin.register(Pacientes)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'email')
    search_fields = ('apellido', 'dni')

@admin.register(EstudiosDisponibles)
class EstudioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

@admin.register(ResultadosdeEstudios)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'mostrar_estudios', 'fecha_estudio', 'bioquimico_responsable')
    def mostrar_estudios(self, obj):
        return ", ".join([e.nombre for e in obj.estudio.all()])
    mostrar_estudios.short_description = 'Estudios Realizados'