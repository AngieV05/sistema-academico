from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Estudiante
from .forms import EstudianteForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EstudianteSerializer

from reportlab.pdfgen import canvas

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes})


def nuevo_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_estudiantes')
    else:
        formulario = EstudianteForm()

    return render(request, 'estudiantes/nuevo_estudiante.html', {'formulario': formulario})


def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)

    if request.method == 'POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_estudiantes')
    else:
        formulario = EstudianteForm(instance=estudiante)

    return render(request, 'estudiantes/nuevo_estudiante.html', {'formulario': formulario})


def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')


@api_view(['GET'])
def lista_estudiantes_api(request):
    estudiantes = Estudiante.objects.all()
    serializer = EstudianteSerializer(estudiantes, many=True)
    return Response(serializer.data)


def reporte_estudiantes_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_estudiantes.pdf"'

    p = canvas.Canvas(response)

    estudiantes = Estudiante.objects.all()

    y = 800

    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 820, "REPORTE DE ESTUDIANTES")

    p.setFont("Helvetica", 11)

    for est in estudiantes:
        texto = f"{est.identificacion} - {est.nombres} {est.apellidos} - Semestre {est.semestre_actual}"
        p.drawString(50, y, texto)
        y -= 20

        if y < 50:
            p.showPage()
            y = 800

    p.save()
    return response