from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import PacienteListView, PacienteDetailView 

urlpatterns = [
    # --- Home y About ---
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # --- Gestión de Pacientes ---
    path('pacientes/', PacienteListView.as_view(), name='lista_pacientes'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/<int:paciente_id>/', PacienteDetailView.as_view(), name='detalle_paciente'),
    path('historia-clinica/', views.historia_clinica, name='historia_clinica'),

    # --- Estudios y Resultados ---
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/registrar/', views.registrar_estudio, name='registrar_estudio'),
    path('resultados/subir/', views.subir_resultado, name='subir_resultado'),

    # --- Autenticación y Registro ---
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro-personal/', views.registro, name='registro'),

    # --- Perfil y Seguridad (Cambio de Contraseña Personalizado) ---
    path('perfil/', views.profile_detail, name='profile_detail'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
    # Esta ruta intercepta el cambio de contraseña con tu vista del código por mail
    path('perfil/seguridad/', views.cambiar_password_seguro, name='password_change'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

    path('paciente/editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='paciente_editar'),
    path('paciente/borrar/<int:pk>/', views.PacienteDeleteView.as_view(), name='paciente_borrar'),
]