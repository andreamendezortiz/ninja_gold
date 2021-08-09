
# Create your views here.
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from time import localtime, strftime

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog número: {number}")

def root(request):
    return redirect("/blogs")

def create(request):
    return redirect("/")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request, number):
    return redirect("/blogs")

def json(request):
    return JsonResponse({
        "name":"Andrea", 
        "age":30
    })

def home(request):
    context = {
        "mostrar": True,
        "imagenes":[
            "https://static.wikia.nocookie.net/kirby/images/c/c8/KirbyAWPortal.png/revision/latest?cb=20200721144852",
            "https://mario.nintendo.com/static/fd723b2893d4d2b39ef71bfdb4e3329c/579b4/mario-background.png", 
            "http://www.dibujoswiki.com/Uploads/dibujoswiki.com/ImagenesGrandes/princesa-zelda-2.jpg", 
            "https://static.wikia.nocookie.net/zelda/images/2/26/Link_Artwork_LAR.png/revision/latest?cb=20191015020845&path-prefix=es"]
        
    }
    return render(request, "home.html", context)

def time(request):
    display = {
        "date": strftime("%d %B %Y", localtime()),
        "time": strftime("%H:%M:%S %p", localtime()),
    }
    return render(request,'home.html', display)
