from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante

        fields = [
            'identificacion',
            'nombres',
            'apellidos',
            'semestre_actual'
        ]