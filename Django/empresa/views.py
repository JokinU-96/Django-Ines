from django.shortcuts import render, redirect

from empresa.models import Empleado, Departamento, Habilidad


# Create your views here.
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empresa/listar_empleados.html', {'empleados': empleados})

def ver_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'empresa/ver_empleado.html', {'empleado': empleado})

def crear_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        antiguedad = request.POST['antiguedad']
        departamento_id = request.POST['departamento_id']
        habilidades_ids = request.POST.getlist('habilidades')

        departamento = Departamento.objects.get(id=departamento_id)
        empleado = Empleado.objects.create(nombre=nombre, fecha_nacimiento=fecha_nacimiento, antiguedad=antiguedad, departamento=departamento)

        empleado.habilidades.set(habilidades_ids)
        return redirect('listar_empleados')

    departamentos = Departamento.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'empresa/crear_empleado.html', {'departamentos':departamentos, 'habilidades':habilidades})
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