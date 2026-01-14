# LaboratorioMinozzi/urls.py

# 1. Imports organizados al comienzo
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

# 2. Única lista de rutas (UNIFICADA)
urlpatterns = [
    # --- Rutas Principales y Navegación ---
    path('', views.home, name='home'),
    path('historia-clinica/', views.historia_clinica, name='historia_clinica'),

    # --- Gestión de Pacientes ---
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/<int:paciente_id>/', views.detalle_paciente, name='detalle_paciente'),

    # --- Gestión de Estudios y Resultados ---
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/registrar/', views.registrar_estudio, name='registrar_estudio'),
    path('resultados/subir/', views.subir_resultado, name='subir_resultado'),

    # --- Sistema de Autenticación de Personal (Independiente del Admin) ---
    path('login/', auth_views.LoginView.as_view(template_name='LaboratoriodeAnalisisClinicosMinozzi/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro-personal/', views.registro, name='registro'),
    path('perfil-personal/', views.profile_detail, name='profile_detail'),
]