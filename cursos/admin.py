from django.contrib import admin
from .models import Profesor, Asignatura, Curso

admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Curso)