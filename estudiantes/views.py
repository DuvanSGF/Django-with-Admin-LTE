# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from estudiantes.models import Estudiante
from estudiantes.forms import EstudianteForm
from estudiantes.filters import EstudianteFilter
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.

@login_required
def inicio(request):
    return render(request, "base/base.html", {})


def login(request):
    if request.user.is_authenticated():
        return redirect('/site')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/site')
            else:
                return render(request, 'registration/login.html', {'error': 'Usuario no existe'}, content_type='text/html')
        else:
            return render(request, 'registration/login.html', {'error': 'Datos invalidos.'}, content_type='text/html')
    else:
        return render(request, 'registration/login.html', {}, content_type='text/html')



def register(request):
	return render(request, "accounts/register.html")


# Vistar para crear un estudiante
class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    template_name = 'estudiantes/add_student.html'
    form_class = EstudianteForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('site:estudiante_listar')


# Vista para Listar los estudiantes
class EstudianteList(LoginRequiredMixin, ListView):
    #queryset = Estudiante.objects.order_by('id_Estudiante')
    template_name = 'estudiantes/student_list.html'
    redirect_field_name = 'redirect_to'
    # Se descomenta la linea de abajo para que funcione el paginado, sin Datables.
    #paginate_by = 5
    def get_queryset(self):
        return Estudiante.objects.filter(Es_Estado=0)


# Vista para actualizar un estudiante
class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiantes/add_student.html'
    success_url = reverse_lazy('site:estudiante_listar')



# Vista para eliminar un estudinates
class EstudianteDelete(LoginRequiredMixin, DeleteView):
    #queryset = Estudiante.objects.update(Es_Estado=1)
    model = Estudiante
    template_name = 'estudiantes/student_delete.html'
    success_url = reverse_lazy('site:estudiante_listar')
    redirect_field_name = 'redirect_to'


# Vista para hacer una vista detalle
class EstudianteShow(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'estudiantes/show_student.html'
    redirect_field_name = 'redirect_to'


# Vista en funcion
@login_required
def search(request):
    estudiante_lista = Estudiante.objects.all()
    estudiante_filtro = EstudianteFilter(request.GET, queryset=estudiante_lista)
    return render(request, 'estudiantes/student_list2.html', {'filter': estudiante_filtro})
