from django.contrib import admin
from stats.models import piloto,carrera,palmares,pole

# Register your models here.


class pilotoadmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')





class carreraadmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

    




class palmaresadmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')



class polesadmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')


admin.site.register(piloto, pilotoadmin)
admin.site.register(carrera, carreraadmin)
admin.site.register(palmares, palmaresadmin)
admin.site.register(pole, polesadmin)









