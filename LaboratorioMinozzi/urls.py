from django.urls import path
from  LaboratorioMinozzi.views import *


urlpatterns = [
    path("", home, name="home")
] 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('estudios/', views.lista_estudios, name="lista_estudios"),
    path('paciente/<int:paciente_id>/', views.detalle_paciente, name="detalle_paciente"),
    path('subir-resultado/', views.subir_resultado, name="subir_resultado"),
]
