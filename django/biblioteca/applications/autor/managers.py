from django.db import models

class AutorManager(models.Manager):
    #def listar_autores(self):
        #return self.all()
    def buscar_autor(self, kword):
        #autor_result = self.filter(nombre=kword) # Se obtiene el registro
        autor_result = self.filter(nombre__icontains=kword) #Busca patron similar 
        return autor_result