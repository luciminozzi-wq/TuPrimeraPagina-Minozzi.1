from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Pacientes, EstudiosDisponibles, ResultadosdeEstudios, Perfil

# --- FORMULARIOS DE NEGOCIO ---

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

class ResultadoEstudioForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Pacientes.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:
        model = ResultadosdeEstudios
        fields = ['paciente', 'estudio', 'fecha_estudio', 'bioquimico_responsable', 'resultado']
        widgets = {
            'estudio': forms.SelectMultiple(attrs={
                'class': 'form-select select-multiple-custom',
                'size': '8'
            }),
            'fecha_estudio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bioquimico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado': forms.FileInput(attrs={'class': 'form-control'}),
        }

class historiaClinicaForm(forms.ModelForm): 
    class Meta:
        model = ResultadosdeEstudios
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'estudio': forms.Select(attrs={'class': 'form-select'}),
            'fecha_estudio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bioquimico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# --- FORMULARIOS DE USUARIO Y PERFIL ---

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# --- FORMULARIO DE SEGURIDAD ---

class PasswordChangeWithCodeForm(PasswordChangeForm):
    codigo_verificacion = forms.CharField(
        max_length=6, 
        label="Código de Verificación",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el código de 6 dígitos'})
    )