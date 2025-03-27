"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path, include

from Django import settings
from autenticacion.views import register, login
from empresa.views import ver_empleado, crear_empleado, eliminar_empleado

urlpatterns = [
    path('login/', login, name='login'),
    path('registrar/', register, name='registrar'),
    path('empresa/', include('empresa.urls'), name='empresa'),

    path('empleados/<int:empleado_id>', ver_empleado, name='ver_empleado'),
    path('empleados/crear/', crear_empleado, name='crear_empleado'),
    path('empleados/eliminar/<int:empleado_id>', eliminar_empleado, name='eliminar_empleado'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
