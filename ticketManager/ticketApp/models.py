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

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='usuarios')

 # Add unique related_names for the ForeignKey fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_set',
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    

class Protocolo(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    description = models.TextField(null=True, blank=True)

    #file field

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    