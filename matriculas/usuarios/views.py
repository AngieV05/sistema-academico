from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def iniciar_sesion(request):

    mensaje = ''

    if request.method == 'POST':

        usuario = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=usuario,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/estudiantes/')
        

        else:

            mensaje = 'Usuario o contraseña incorrectos'

    return render(
        request,
        'usuarios/login.html',
        {'mensaje': mensaje}
    )


def cerrar_sesion(request):

    logout(request)

    return redirect('login')