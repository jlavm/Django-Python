from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseNotFound
from models import Photo, VISIBILITY_PUBLIC, VISIBILITY_PRIVATE
from forms import LoginForm, PhotoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator

# Create your views here.

class HomeView(View):

    def get(self,request):

        """
        Se ejecuta en /HelloWorld
        param: request: objeto request
        return objeto: response
        """
        #Obtenemos todas las imagenes

        photo_list = Photo.objects.all().filter(visibility=VISIBILITY_PUBLIC).order_by('-createdAt')
        context = {
            'photos': photo_list[:8]
        }
        return render(request,'Photos/index.html',context)

class PhotoDetail(View):

    def get(self,request,pk):

        """
        Muestra detalle de una foto
        param: request: objeto request
        param: pk: id foto
        return objeto: response
        """

        possible_photos= Photo.objects.filter(pk=pk)

        if request.user.is_authenticated():
            possible_photos = possible_photos.filter(Q(owner=request.user) | Q(visibility=VISIBILITY_PUBLIC))
        else:
             possible_photos = possible_photos.filter(visibility=VISIBILITY_PUBLIC)

        if len(possible_photos) == 0:

            return HttpResponseNotFound("No existe la foto seleccionada")
        else:
            context = {
                'photo':possible_photos[0]
            }
            return render(request,'photos/photo_detail.html',context)

class UserLogin(View):

    def get(self,request):
        login_form = LoginForm()

        context = {
        'form': login_form,
         }
        return render(request,'photos/login.html',context)

    def post(self,request):

        error_messages = []

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is None:
                error_messages.append("Nombre de usuario o contrasena incorrectos")
            else:
                if user.is_active:
                    login(request,user) #crea sesion usuario
                    next_url = request.GET.get('next','/')
                    return redirect(next_url)
                else:
                     error_messages.append("El usuario no esta activo")


        context = {
            'form': login_form,
            'errors': error_messages

        }

        return render(request,'photos/login.html',context)

class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect("/")

class UserProfile(View):

    @method_decorator(login_required()) #forzamos a que el usuario este autenticado

    def get(self,request):

        context = {

            'photos':request.user.photo_set.all()
        }

        return render(request,'photos/profile.html',context)


@login_required() #forzamos a que el usuario este autenticado

def create_photo(request):

    new_photo = None

    if request.method == 'POST':
        photo_with_user = Photo(owner=request.user) #Creamos foto con usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_user)

        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()

    else:
        form = PhotoForm()

    context = {

        'form': form,
        'photo': new_photo
    }

    return render(request,'photos/create_photo.html',context)

class PhotoListView(ListView):

    model = Photo
    template_name = 'photos/photo_list.html'