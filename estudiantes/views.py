# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from estudiantes.models import Estudiante
from estudiantes.forms import EstudianteForm
from estudiantes.filters import EstudianteFilter

# Create your views here.
def inicio(request):
    return render(request, "base/base.html", {})

# Vistar para crear un estudiante
class EstudianteCreate(CreateView):
    model = Estudiante
    template_name = 'estudiantes/add_student.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('site:estudiante_listar')


# Vista para Listar los estudiantes
class EstudianteList(ListView):
    queryset = Estudiante.objects.order_by('id_Estudiante')
    #queryset = Estudiante.objects.filter(Es_Estado=0).order_by('id_Estudiante')
    template_name = 'estudiantes/student_list.html'
    #paginate_by = 5


# Vista para actualizar un estudiante
class EstudianteUpdate(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiantes/add_student.html'
    success_url = reverse_lazy('site:estudiante_listar')


# Vista para eliminar un estudinates
class EstudianteDelete(DeleteView):
    #queryset = Estudiante.objects.update(Es_Estado=1)
    model = Estudiante
    template_name = 'estudiantes/student_delete.html'
    success_url = reverse_lazy('site:estudiante_listar')


# Vista para hacer una vista detalle
class EstudianteShow(DetailView):
    model = Estudiante
    template_name = 'estudiantes/show_student.html'


# Vista en funcion
def search(request):
    estudiante_lista = Estudiante.objects.all()
    estudiante_filtro = EstudianteFilter(request.GET, queryset=estudiante_lista)
    return render(request, 'estudiantes/student_list2.html', {'filter': estudiante_filtro})
