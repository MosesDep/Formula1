from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey

# Create your models here.



class piloto(models.Model):

    nombre=models.CharField(primary_key=True, max_length=50)
    foto=models.ImageField(upload_to="stats", null=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    nacimiento=models.DateTimeField()
    update=models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name="piloto"
        verbose_name_plural="pilotos"



    def __str__(self) :
        return self.nombre


class carrera(models.Model):

    idnombre=ForeignKey(piloto, on_delete=models.CASCADE)
    ano=models.PositiveIntegerField(null=True)
    nombre=models.CharField(max_length=50)
    posicicion=models.PositiveIntegerField()
    foto=models.ImageField(upload_to="stats", null=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)
    icono=models.ImageField(upload_to="stats", null=True, blank=True)




    class Meta:

        verbose_name="carrera"
        verbose_name_plural="carreras"
        ordering = ['-ano']




class palmares(models.Model):
    idnombre=ForeignKey(piloto, on_delete=models.CASCADE)
    titulos=models.PositiveIntegerField()
    victoias=models.PositiveIntegerField()
    poles=models.PositiveIntegerField()
    abandonos=models.PositiveIntegerField()
    vueltasr=models.PositiveIntegerField()
    inicio=models.DateTimeField()
    retiro=models.DateTimeField(null=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name="palmares"
        verbose_name_plural="palmares"





class pole(models.Model):


    idnombre=ForeignKey(piloto, on_delete=models.CASCADE)
    ano=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    posicicion=models.PositiveIntegerField()
    foto=models.ImageField(upload_to="stats", null=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)


    class Meta:

        verbose_name="pole"
        verbose_name_plural="poles"



        



        