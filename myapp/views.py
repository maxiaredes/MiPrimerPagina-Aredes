from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'message': 'Bienvenidos a mi aplicacion de Viajes con Django'
    }
    return render(request, 'myapp/index.html', context)