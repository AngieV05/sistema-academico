from django.db import models

class Estudiante(models.Model):
    identificacion = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    semestre_actual = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"