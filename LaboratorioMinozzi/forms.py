from django import forms
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
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
        fields = ['paciente', 'estudio', 'fecha_estudio', 'resultado', 'bioquimico_responsable']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'estudio': forms.Select(attrs={'class': 'form-select'}),
            'fecha_estudio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'resultado': forms.FileInput(attrs={'class': 'form-control'}),
            'bioquimico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Esto personaliza el texto dentro del select para que veas el DNI
        self.fields['paciente'].label_from_instance = lambda obj: f"{obj.DNI} - {obj.nombre} {obj.apellido}"
        self.fields['estudio'].label_from_instance = lambda obj: f"{obj.nombre}"

class historiaClinicaForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido', 'DNI']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
        }