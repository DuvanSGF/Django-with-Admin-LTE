from django.conf.urls import url
from .views import inicio
from estudiantes.views import EstudianteCreate, EstudianteList, EstudianteDelete, EstudianteUpdate, EstudianteShow, search

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^nuevo/', EstudianteCreate.as_view(), name='estudiante_crear'),
    url(r'^listar', EstudianteList.as_view(), name='estudiante_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', EstudianteDelete.as_view(), name='estudiante_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', EstudianteUpdate.as_view(), name='estudiante_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', EstudianteShow.as_view(), name='estudiante_mostrar'),
    url(r'^buscar/$', search, name='estudiante_buscar'),
]
