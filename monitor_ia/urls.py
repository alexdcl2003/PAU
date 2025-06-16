from django.urls import path
from . import views 

urlpatterns = [
    path('analizar-imagen/', views.analizar_frame, name='analizar_frame'),
]