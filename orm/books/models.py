from django.db import models
from authors.models import Author

#Relación uno a muchos con autores

class Book(models.Model):
    title = models.CharField(max_length=50)
    #primer argumento el modelo con el que hacemos la relación
    #on_delete = CASCADE cuando borro un author tambien la reciones con los libros
    author = models.ForeignKey(Author,on_delete=models.CASCADE , related_name = 'books' )
    
    pages = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# La fundación - yo robot - La ultima pregunta
# it , el resplandor , la torre oscura        
