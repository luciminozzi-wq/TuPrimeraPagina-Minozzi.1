from django.db import models

class EstudiosDisponibles(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    DNI = models.CharField(max_length=20, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class ResultadosdeEstudios(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    estudio = models.ForeignKey(EstudiosDisponibles, on_delete=models.CASCADE)
    fecha_estudio = models.DateTimeField()
    resultado = models.FileField(upload_to='resultados_pdfs/')
    fecha_resultado = models.DateTimeField(auto_now_add=True)
    bioquimico_responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"Resultado de {self.estudio.nombre} para {self.paciente.nombre} {self.paciente.apellido}"
    