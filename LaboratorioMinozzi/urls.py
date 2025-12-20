from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('historia-clinica/', views.historia_clinica, name='historia_clinica'), # Añade esta
    path('subir-resultado/', views.subir_resultado, name='subir_resultado'),
]