from django.shortcuts import render
from . models import videojuegos
from django.views import generic

#formulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    num_Juegos = videojuegos.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_juegos': num_Juegos}
    )
def steam(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'steam.html',
        context={'num_juegos': num_Juegos},
    )
def origin(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'origin.html',
        context={'num_juegos': num_Juegos},
    )
def wallet2(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'wallet2.html',
        context={'num_juegos': num_Juegos},
    )

def preguntas(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'preguntas.html',
        context={'num_juegos': num_Juegos},
    )

def contacto(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'contacto.html',
        context={'num_juegos': num_Juegos},
    )

def red(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'red.html',
        context={'num_juegos': num_Juegos},
    )

def fallguys(request):
    num_Juegos = videojuegos.objects.all().count()
    

    return render(
        request,
        'fallguys.html',
        context={'num_juegos': num_Juegos},
    )

class GameCreate(CreateView):
    model = videojuegos
    fields = ['name', 'pegi']

class GameUpdate(UpdateView):
    model = videojuegos
    fields = ['name','pegi']

class GameDelete(DeleteView):
    model = videojuegos
    success_url = reverse_lazy('index')



from django.views import generic


class GameListView(generic.ListView):
    model = videojuegos
    paginate_by = 20


class GameDetailView(generic.DetailView):
    model = videojuegos