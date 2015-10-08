from django.contrib import admin
from concesionario.apps.orden_de_trabajo.models import OrdenDeTrabajo
# Register your models here.

class AdminOrdenDeTrabajo (admin.ModelAdmin):
	#atributos
	list_display = ('id', 'empleado', 'cliente',
		 'placa', 'fecha_entrada', 'fecha_salida', 'descripcion','estado_reparacion')
	#atributos por los que se buscara
	search_fields = ('id', 'placa')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(OrdenDeTrabajo, AdminOrdenDeTrabajo)