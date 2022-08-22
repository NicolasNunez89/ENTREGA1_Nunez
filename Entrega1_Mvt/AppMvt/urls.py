from django.urls import path

from AppMvt import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('buscarProfesor',  views.buscarProfesor, name="buscarProfesor"),
    path('buscar/', views.buscar),
]

