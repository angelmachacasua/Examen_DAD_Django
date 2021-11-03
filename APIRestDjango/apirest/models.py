from django.db import models


class Trabajador(models.Model):

    nombres=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=20, null=True)
    direccion=models.CharField(max_length=50, null=True)
    especialidad=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    area=models.CharField(max_length=50, null=True)

    class Meta:
        
        verbose_name = ("Trabajador")
        verbose_name_plural = ("Trabajadores")

    def __str__(self):
        return self.nombres
