from django.shortcuts import render
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