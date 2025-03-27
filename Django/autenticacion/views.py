import django
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from autenticacion.forms import RegisterForm, LoginForm
from autenticacion.models import CustomUser

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                django.contrib.auth.login(request, user)
            return redirect('listar_empleados')
    else:
        form = LoginForm()
    return render(request, 'autenticacion/login.html', {'form': form})
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'El email ya está registrado.')
                return render(request, 'autenticacion/registro.html', {'form': form})
            grupo = Group.objects.get(name="Empleado")
            user = CustomUser.objects.create_user(email=email, password=password, name=name)
            user.groups.add(grupo)
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
            # Asigna automáticamente al grupo "Empleado"
        else:
            return render(request, 'autenticacion/registro.html', {'form': form})
    form = RegisterForm()
    return render(request, 'autenticacion/registro.html', {'form': form})

def logout(request):
    django.contrib.auth.logout(request)
    return redirect('listar_empleados')