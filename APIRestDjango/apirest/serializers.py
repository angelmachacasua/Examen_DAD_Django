from rest_framework import fields, serializers
from .models import Trabajador

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Trabajador
        fields=['id','nombres','dni','celular','direccion','especialidad','email','area']
        #fields ='__all__'