from django.urls import path
from . import views

urlpatterns = [

    path('', views.lista_estudiantes, name='lista_estudiantes'),

    path('nuevo/', views.nuevo_estudiante, name='nuevo_estudiante'),

    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),

    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('api/estudiantes/', views.lista_estudiantes_api, name='api_estudiantes'),

    path('reporte/pdf/', views.reporte_estudiantes_pdf, name='reporte_estudiantes_pdf'),

]