from django.shortcuts import render


def palestras(request):
    return render(request, 'eventos/palestras.html')

def minicursos(request):
    return render(request, 'eventos/minicursos.html')

def visitas(request):
    return render(request, 'eventos/visitas.html')
