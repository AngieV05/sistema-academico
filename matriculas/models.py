from django.db import models
from estudiantes.models import Estudiante
from cursos.models import Curso, Asignatura


class AsignaturaCursada(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota_final = models.FloatField()

    def __str__(self):
        return f"{self.estudiante} - {self.asignatura}"


class CursoMatriculado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    periodo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    nota_final = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"