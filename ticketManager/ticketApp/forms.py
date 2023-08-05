from django.forms  import *


from .models import Protocolo

class CreateProtocolForm(ModelForm):
    class Meta:
        model = Protocolo
        fields = '__all__'