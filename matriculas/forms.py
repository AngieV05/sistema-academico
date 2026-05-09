from django import forms
from .models import CursoMatriculado


class CursoMatriculadoForm(forms.ModelForm):

    class Meta:

        model = CursoMatriculado

        fields = [
            'curso',
            'periodo',
            'estado',
            'nota_final'
        ]