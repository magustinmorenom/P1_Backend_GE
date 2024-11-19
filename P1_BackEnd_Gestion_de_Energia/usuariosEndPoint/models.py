from django.db import models

class usuariosModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    pictureurl = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.nombre
