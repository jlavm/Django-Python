from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseNotFound
from models import Photo, VISIBILITY_PUBLIC, VISIBILITY_PRIVATE

# Create your views here.

def home(request):

    """
    Se ejecuta en /HelloWorld
    param: request: objeto request
    return objeto: response
    """
    html='<strong>Hola Mundo</strong>'
    return HttpResponse(html)

def home2(request):

    """
    Se ejecuta en /HelloWorld
    param: request: objeto request
    return objeto: response
    """
    #Obtenemos todas las imagenes

    photo_list = Photo.objects.all().filter(visibility=VISIBILITY_PUBLIC).order_by('-createdAt')
    context = {
        'photos': photo_list[:3]
    }
    return render(request,'Photos/index.html',context)

def photo_detail(request,pk):

    """
    Muestra detalle de una foto
    param: request: objeto request
    param: pk: id foto
    return objeto: response
    """

    possible_photos = Photo.objects.filter(pk=pk, visibility=VISIBILITY_PUBLIC)

    if len(possible_photos) == 0:

        return HttpResponseNotFound("No existe la foto seleccionada")
    else:
        context = {
            'photo':possible_photos[0]
        }
        return render(request,'photos/photo_detail.html',context)

def user_login(request):

    error_messages = []

    if request.method == 'POST':
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        user = authenticate(username=username,password=password)
        if user is None:
            error_messages.append("Nombre de usuario o contrasena incorrectos")
        else:
            if user.is_active:
                login(request,user) #crea sesion usuario
                return redirect('/')
            else:
                 error_messages.append("El usuario no esta activo")


    context = {
        'errors': error_messages
    }

    return render(request,'photos/login.html',context)


def user_logout(request):
    logout(request)
    return redirect("/")