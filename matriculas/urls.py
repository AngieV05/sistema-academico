from django.urls import path

from .views import matricular_curso

urlpatterns = [

    path(
        'matricular/<int:estudiante_id>/',
        matricular_curso,
        name='matricular_curso'
    ),

]