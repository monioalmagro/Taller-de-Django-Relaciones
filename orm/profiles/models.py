from django.db import models
from authors.models import Author

#Relación uno a uno con author

class Profile(models.Model):
    alias = models.CharField(max_length=50)

    author = models.OneToOneField(Author,on_delete = models.CASCADE, default=None)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alias
    