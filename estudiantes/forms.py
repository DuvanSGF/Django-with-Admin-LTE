from django import forms
from estudiantes.models import Estudiante
from django.forms.utils import flatatt

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'Es_Nombre',
            'Es_Apellido',
            'Es_TipoID',
            'Es_Identificacion',
            'Es_Codigo',
            'Es_Programa_ID',
            'Es_Departamento',
            'Es_Municipio',
            'Es_Venada',
        ]

        labels = {
            'Es_Nombre': 'Nombre:',
            'Es_Apellido': 'Apellidos',
            'Es_TipoID': 'Tipo de identificacion',
            'Es_Identificacion': 'Numero de ID',
            'Es_Codigo': 'Codigo',
            'Es_Programa_ID': 'Selecciona tu programa:',
            'Es_Departamento': 'Selecciona tu Departamento',
            'Es_Municipio': 'Selecciona tu municipio',
            'Es_Venada': 'Comes en la Avenada',
        }


	widgets  =  {

    			'Es_Nombre': forms.TextInput(attrs={'class':'form-control'}),
    			'Es_Apellido': forms.TextInput(attrs={'class':'form-control'}),
                'Es_TipoID': forms.Select(attrs={'class':'form-control'}),
                'Es_Identificacion': forms.NumberInput(attrs={'class':'form-control'}),
    			'Es_Codigo': forms.NumberInput(attrs={'class':'form-control'}),
    			'Es_Programa_ID': forms.Select(attrs={'class':'form-control'}),
                'Es_Departamento': forms.Select(attrs={'class':'form-control'}),
                'Es_Municipio': forms.Select(attrs={'class':'form-control'}),
    			'Es_Venada': forms.Select(attrs={'class':'form-control'}),

		}

def clean(self, *arg, **kwargs):
    cleaned_data = super(EstudianteForm, self).clean(*arg, **kwargs)
