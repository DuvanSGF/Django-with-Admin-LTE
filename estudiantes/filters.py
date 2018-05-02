import django_filters
from estudiantes.models import Estudiante

class EstudianteFilter(django_filters.FilterSet):
	class Meta:
		model = Estudiante
		fields = ['Es_Nombre', 'Es_Apellido', 'Es_Identificacion', 'Es_Codigo']
