from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):

    """
    Se ejecuta en /HelloWorld
    param: request: objeto request
    return objeto: response
    """
    html='<strong>Hola Mundo</strong>'
    return HttpResponse(html)