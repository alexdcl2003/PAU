# reconocimiento/views.py
from django.shortcuts import render

# Vista para el reconocimiento (ya está definida)
def dashboard(request):
    return render(request, 'core/reconocimiento/dashboard.html')

def monitor(request):
    return render(request, 'core/reconocimiento/monitor.html')

def reportes(request):
    return render(request, 'core/reconocimiento/reportes.html')

def usuarios(request):
    return render(request, 'core/reconocimiento/usuarios.html')

def configuracion(request):
    return render(request, 'core/reconocimiento/configuracion.html')