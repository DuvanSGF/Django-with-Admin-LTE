from django import forms
from estudiantes.models import Estudiante
from django.forms.utils import flatatt

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'Es_Nombre',
            'Es_Apellido',
            'Es_Codigo',
            'Es_Programa_ID',
            'Es_Departamento_ID',
            'Es_Municipio_ID',
            'Es_Venada',
        ]

        labels = {
            'Es_Nombre': 'Nombre:',
            'Es_Apellido': 'Apellidos',
            'Es_Codigo': 'Codigo',
            'Es_Programa_ID': 'Selecciona tu programa:',
            'Es_Departamento_ID': 'Selecciona tu Departamento',
            'Es_Municipio_ID': 'Selecciona tu municipio',
            'Es_Venada': 'Comes en la Avenada',
        }


	widgets  =  {

    			'Es_Nombre': forms.TextInput(attrs={'class':'form-control'}),
    			'Es_Apellido': forms.TextInput(attrs={'class':'form-control'}),
    			'Es_Codigo': forms.NumberInput(attrs={'class':'form-control'}),
    			'Es_Programa_ID': forms.Select(attrs={'class':'form-control'}),
    			'Es_Municipio_ID': forms.Select(attrs={'class':'form-control'}),
    			'Es_Venada': forms.Select(attrs={'class':'form-control'}),

		}
