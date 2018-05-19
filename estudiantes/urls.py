from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
#from django.contrib import admin
from estudiantes.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', inicio, name="inicio"),
    url(r'^login/$', login, name='login'),
    #url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,  {'next_page': '/site/'}, name='logout'),
    url(r'^register/$', register, name ='user_register'),
    url(r'^nuevo/', EstudianteCreate.as_view(), name='estudiante_crear'),
    url(r'^listar', EstudianteList.as_view(), name='estudiante_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', EstudianteDelete.as_view(), name='estudiante_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', EstudianteUpdate.as_view(), name='estudiante_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', EstudianteShow.as_view(), name='estudiante_mostrar'),
    url(r'^buscar/$', search, name='estudiante_buscar'),
    #url(r'^admin', admin, name="logout"),
]
