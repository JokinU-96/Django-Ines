from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from autenticacion.utils import es_gerente
from empresa.forms import EmpleadoFormulario
from empresa.models import Empleado, Departamento, Habilidad


# Create your views here.
def listar_empleados(request):
    empleados = Empleado.objects.all()
    paginator = Paginator(empleados, 2)
    page = request.GET.get('page', 1)
    empleados_paginados = paginator.get_page(page)
    return render(request, 'empresa/listar_empleados.html', {'empleados': empleados_paginados})


def ver_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'empresa/ver_empleado.html', {'empleado': empleado})

@login_required
@user_passes_test(es_gerente)
def crear_empleado(request):
    if request.method == 'POST' and request.FILES:
        form = EmpleadoFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoFormulario()

    departamentos = Departamento.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'empresa/crear_empleado.html',
                  {'form': form, 'departamentos': departamentos, 'habilidades': habilidades})


def eliminar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.delete()
    return redirect('listar_empleados')


def editar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)

    if request.method == 'POST':
        nombre = request.POST['nombre']
        departamento_id = request.POST['departamento_id']
        habilidades_ids = request.POST.getlist('habilidades')
        departamento = Departamento.objects.get(id=departamento_id)
        empleado.habilidades.set(habilidades_ids)
        empleado.save()
        return redirect('listar_empleados')

    departamentos = Departamento.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'empresa/editar_empleado.html', {
        empleado: empleado,
        departamentos: departamentos,
        habilidades: habilidades
    })
