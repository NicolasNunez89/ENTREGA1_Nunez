from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppMvt.forms import EntregableFormulario,ProfesorFormulario,EstudianteFormulario
from AppMvt.models import Profesor,Estudiante, Entregable


# Create your views here.
def inicio(request):
    
      return render(request, "inicio.html")
  
def estudiantes(request):
    
    if request.method == 'POST':
    
            miFormulario = EstudianteFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  profesor = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  profesor.save()

                  return render(request, "inicio.html") 

    else:

            miFormulario= EstudianteFormulario() 

    return render(request, "carga_Profesor.html", {"miFormulario":miFormulario})


def entregables(request):

    if request.method == 'POST':
        
            miFormulario = EntregableFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  FEntregable = Entregable (nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'],
                   entregado=informacion['entregado']) 

                  FEntregable.save()

                  return render(request, "inicio.html") 

    else:

            miFormulario= EntregableFormulario() 

    return render(request, "carga_Entregable.html", {"miFormulario":miFormulario})


def profesores(request):
    
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion'],legajo=informacion['legajo']) 

                  profesor.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "carga_Profesor.html", {"miFormulario":miFormulario})
  
  

def buscarProfesor(request):
    return render(request, "buscarProfesor.html")

def buscar(request):
    
      if  request.GET["legajo"]:
    
            legajo = request.GET['legajo'] 
            profesor = Profesor.objects.filter(legajo__icontains=legajo)

            return render(request, "inicio.html", {"Profesor": profesor})

      else: 

	      respuesta = "No enviaste datos"

      return HttpResponse(respuesta)