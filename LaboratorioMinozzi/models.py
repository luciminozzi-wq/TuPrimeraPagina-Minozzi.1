from django.db import models

class EstudiosDisponibles(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    DNI = models.CharField(max_length=20, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.DNI} - {self.nombre} {self.apellido}"

class ResultadosdeEstudios(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    estudio = models.ManyToManyField(EstudiosDisponibles)
    fecha_estudio = models.DateField()
    bioquimico_responsable = models.CharField(max_length=100)
    resultado = models.FileField(upload_to='resultados/')
    fecha_resultado = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Resultado {self.paciente.apellido} - {self.fecha_estudio}"
    
    