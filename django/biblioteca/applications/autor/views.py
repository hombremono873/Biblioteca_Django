from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    #model = Autor  Si lo quitamos podemos usar get_queryset(self) para acceder a los datos
    context_object_name = 'autores'
    template_name = 'autor/lista.html'
        
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        return Autor.objects.buscar_autor(palabra_clave)
    

    
 