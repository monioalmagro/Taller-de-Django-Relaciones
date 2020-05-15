from django.db import models
from books.models import Book
from authors.models import Author

#Relación muchos a muchos con libros

class Gender(models.Model):
    name = models.CharField(max_length=50)
    
    books = models.ManyToManyField(Book,related_name = 'books')

    authors = models.ManyToManyField(Author, through='AuthorGender')

    create_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

class AuthorGender(models.Model):
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    
 


