from django.db import models

class Profesor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    numero_creditos = models.IntegerField()
    prerrequisito = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    aula = models.CharField(max_length=20)
    horario = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.profesor.nombres}"