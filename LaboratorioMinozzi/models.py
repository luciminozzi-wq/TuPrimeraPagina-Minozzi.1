from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class EstudiosDisponibles(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50) # CharField 1
    apellido = models.CharField(max_length=50) # CharField 2
    dni = models.IntegerField(unique=True) # Integer Unique
    email = models.EmailField()
    fecha_nacimiento = models.DateField() # Campo de Fecha
    foto = models.ImageField(upload_to='pacientes/', null=True, blank=True) # Campo de Imagen

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class ResultadosdeEstudios(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    estudio = models.ManyToManyField(EstudiosDisponibles)
    fecha_estudio = models.DateField()
    bioquimico_responsable = models.CharField(max_length=100)
  
    resultado = models.FileField(upload_to='resultados/')
    
    fecha_resultado = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Resultado {self.paciente.apellido} - {self.fecha_estudio}"

    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}" 
    
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
  if hasattr(instance, 'perfil'):  
    instance.perfil.save()
post_save.connect(guardar_perfil, sender=User)
post_save.connect(crear_perfil, sender=User)
