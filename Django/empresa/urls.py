from django.contrib.auth.decorators import user_passes_test
from django.urls import path

from autenticacion.utils import es_gerente
from autenticacion.views import logout, register
from .views import listar_empleados, ver_empleado, crear_empleado, editar_empleado


urlpatterns = [
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('empleados/', listar_empleados, name='listar_empleados'),
    path('empleados/<int:empleado_id>',ver_empleado, name='ver_empleado'),
    path('empleados/crear',user_passes_test(es_gerente)(crear_empleado), name='crear_empleado'),
    path('empleados/editar/<int:empleado_id>',editar_empleado, name='editar_empleado'),

]