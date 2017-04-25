from django.shortcuts import render
from django.views import generic
from .models import Palestra, VisitaTecnica, MiniCurso


# def palestras(request):
#     return render(request, 'eventos/palestras.html')
#
# def minicursos(request):
#     return render(request, 'eventos/minicursos.html')
#
# def visitas(request):
#     return render(request, 'eventos/visitas.html')

class PalestrasView(generic.ListView):
    model = Palestra
    template_name = 'eventos/palestras.html'
    context_object_name = 'all_palestras'

    def get_queryset(self):
        return Palestra.objects.all()

class VisitasView(generic.ListView):
    model = VisitaTecnica
    template_name = 'eventos/visitas.html'
    context_object_name = 'all_visitas'

    def get_queryset(self):
        return VisitaTecnica.objects.all()

class MiniCursoView(generic.ListView):
    model = MiniCurso
    template_name = 'eventos/minicursos.html'
    context_object_name = 'all_minicursos'

    def get_queryset(self):
        return MiniCurso.objects.all()
