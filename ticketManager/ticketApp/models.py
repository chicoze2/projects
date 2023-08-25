from django.db import models

from  django.contrib.auth.models import AbstractUser


class Empresa(models.Model):
    name = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length = 254, null=True, default=None)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='usuarios', default=None , null=True)
    supervisor =  models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    

class Protocolo(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='protocolos')

    description = models.TextField(null=True, blank=True)

    #file field

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    