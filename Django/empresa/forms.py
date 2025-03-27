from django import forms

from empresa.models import Empleado


class EmpleadoFormulario(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'departamento', 'habilidades', 'antiguedad', 'imagen']
#Es posible crear funciones para limitar el tipo de fichero que se sube al sitio.
#Tambien es común renombrar los archivos a la hora de subirlos. (Ej. con la fecha de subida)