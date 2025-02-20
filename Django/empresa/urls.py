from django.urls import path
from .views import listar_empleados, ver_empleado, crear_empleado, editar_empleado


urlpatterns = [
    path('empleados', listar_empleados, name='listar_empleados'),
    path('empleados/<int:empleado_id>',ver_empleado, name='ver_empleado'),
    path('empleados/crear',crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:empleado_id>',editar_empleado, name='editar_empleado'),

]