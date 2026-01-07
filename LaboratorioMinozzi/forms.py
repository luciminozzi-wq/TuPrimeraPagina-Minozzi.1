from django import forms
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        # Agregué los campos exactos de tu modelo Pacientes
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono', 'DNI']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = EstudiosDisponibles
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = ResultadosdeEstudios
        # Campos corregidos según tu models.py
        fields = ['paciente', 'estudio', 'fecha_estudio', 'resultado', 'bioquimico_responsable']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'estudio': forms.Select(attrs={'class': 'form-control'}),
            'fecha_estudio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'resultado': forms.FileInput(attrs={'class': 'form-control'}),
            'bioquimico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }

class historiaClinicaForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido', 'DNI']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
        }