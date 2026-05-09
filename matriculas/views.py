from django.shortcuts import render, redirect

from estudiantes.models import Estudiante
from .models import CursoMatriculado
from .forms import CursoMatriculadoForm


def matricular_curso(request, estudiante_id):

    estudiante = Estudiante.objects.get(id=estudiante_id)

    if request.method == 'POST':

        formulario = CursoMatriculadoForm(request.POST)

        if formulario.is_valid():

            matricula = formulario.save(commit=False)

            matricula.estudiante = estudiante

            matricula.save()

            return redirect('lista_estudiantes')

    else:

        formulario = CursoMatriculadoForm()

    return render(
        request,
        'matriculas/matricular_curso.html',
        {
            'formulario': formulario,
            'estudiante': estudiante
        }
    )