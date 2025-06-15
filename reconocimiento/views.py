# reconocimiento/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'core/reconocimiento/dashboard.html')

@login_required
def monitor(request):
    return render(request, 'core/reconocimiento/monitor.html')

@login_required
def reportes(request):
    return render(request, 'core/reconocimiento/reportes.html')

@login_required
def usuarios(request):
    return render(request, 'core/reconocimiento/usuarios.html')

@login_required
def configuracion(request):
    return render(request, 'core/reconocimiento/configuracion.html')

