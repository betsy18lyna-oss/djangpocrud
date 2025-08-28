from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home (request):
    return render(request, "home.html")
def signup(request):
    if request.method == "GET":
        return render(request,
                   "signup.html",
                  {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST ["password2"]:
            try:
                user = User.objects.create_user(request.POST ["username"],
                                                request.POST ["password1"])
                user.save
                return HttpResponse("Usuario ha sido creado de manera exitosa")
            except:
                return HttpResponse("Error al crear el usuario")
        else:
            return HttpResponse ("La contraseña no coinciden. Verificar ")