from django.shortcuts import render

def reconocimiento(request):
   
    return render(request, 'core/reconocimiento/reconocimiento.html')