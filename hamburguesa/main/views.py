from django.shortcuts import render

# Create your views here.

def home(request):  # Define una función llamada 'home' que toma un objeto 'request' como argumento.
    return render(request, 'feane-1.0.0/index.html')  # Devuelve el resultado de renderizar 'index.html' con el objeto 'request'.

