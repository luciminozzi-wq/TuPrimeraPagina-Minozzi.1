"""
URL configuration for LaboratoriodeAnalisisClinicosMinozzi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from LaboratorioMinozzi import views as laboratorio_views # Importamos tus vistas con un nombre distinto

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Usamos 'laboratorio_views' para que Django sepa que debe buscar en TU views.py
    path('accounts/password_change/', laboratorio_views.cambiar_password_seguro, name='password_change'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('LaboratorioMinozzi.urls')),   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)