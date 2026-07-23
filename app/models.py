from django.db import models

# Create your models here. 

class Health(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=155)
    password = models.CharField(max_length=55)
    contact = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name