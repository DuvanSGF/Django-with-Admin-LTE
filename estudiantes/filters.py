import django_filters
from estudiantes.models import Estudiante

class EstudianteFilter(django_filters.FilterSet):
	class Meta:
		model = Estudiante
		fields = ['Es_Nombre', 'Es_Apellido', 'Es_Codigo', 'Es_Programa_ID', 'Es_Departamento_ID', 'Es_Municipio_ID', 'Es_Venada']
