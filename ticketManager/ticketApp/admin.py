from django.contrib import admin

# Register your models here.
from .models import User, Empresa, Protocolo

admin.site.register(Empresa)
admin.site.register(User)
admin.site.register(Protocolo)
