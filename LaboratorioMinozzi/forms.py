from django import forms
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido', 'DNI', 'email', 'telefono', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre'}),
            'DNI': forms.NumberInput(attrs={'placeholder': 'DNI sin puntos'}),
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = EstudiosDisponibles
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }

class ResultadoEstudioForm(forms.ModelForm):
    class Meta:
        model = ResultadosdeEstudios
        fields = ['paciente', 'estudio', 'fecha_estudio', 'resultado', 'bioquimico_responsable']
        widgets = {
            'fecha_estudio': forms.DateInput(attrs={'type': 'date'}),
        }

class historiaClinicaForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido', 'DNI', 'email', 'telefono', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    