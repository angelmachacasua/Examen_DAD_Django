from django.shortcuts import render

from rest_framework import serializers, viewsets
#from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.generics import ListAPIView
from .serializers import TrabajadorSerializer
from .models import Trabajador

class TrabajadorViewSet (viewsets.ModelViewSet):
    queryset=Trabajador.objects.all();
    serializer_class=TrabajadorSerializer
#class ListTrabajadores(ListAPIView):
    #query = Trabajador.objects.all
    #serializers_class = TrabajadorSerializer
#class CreateTrabajador(CreateAPIView):
   # queryset = Trabajador.objects.all()
   # serializers_class = TrabajadorSerializer

#class UpdateTrabajador(UpdateAPIView):
   #queryset = Trabajador.objects.all()
   # serializers_class = TrabajadorSerializer
#class deleteTrabajador(DestroyAPIView):
    #queryset = Trabajador.objects.all()
    #serializers_class = TrabajadorSerializer