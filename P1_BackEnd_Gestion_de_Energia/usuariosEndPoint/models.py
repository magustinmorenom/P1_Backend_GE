from django.db import models

class usuariosModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
    
