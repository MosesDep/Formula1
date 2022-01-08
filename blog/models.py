from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class blog(models.Model):


    titulo=models.CharField(primary_key=True, max_length=100)
    autor=models.CharField( max_length=100)
    foto=models.ImageField(upload_to="blog", null=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:

        verbose_name="blog"
        verbose_name_plural="blogs"
        ordering = ['-created']

        def __str__(self) :
            return self.nombre




class contenido(models.Model):

    idtitulo=models.ForeignKey(blog, on_delete=models.CASCADE)
    contenido=models.TextField()


    class Meta:

        verbose_name="contenido"
        verbose_name_plural="contenidos"
