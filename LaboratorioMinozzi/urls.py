from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
# Importamos las clases (CBV) que creamos en views.py
from .views import PacienteListView, PacienteDetailView 

urlpatterns = [
    # --- Páginas Generales ---
    path('', views.home, name='home'),
    path('historia-clinica/', views.historia_clinica, name='historia_clinica'),
    path('pacientes/', PacienteListView.as_view(), name='lista_pacientes'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/<int:paciente_id>/', PacienteDetailView.as_view(), name='detalle_paciente'),
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/registrar/', views.registrar_estudio, name='registrar_estudio'),
    path('resultados/subir/', views.subir_resultado, name='subir_resultado'),
    path('login/', auth_views.LoginView.as_view(template_name='LaboratoriodeAnalisisClinicosMinozzi/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro-personal/', views.registro, name='registro'),
    path('perfil/', views.profile_detail, name='profile_detail'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]