from django.contrib import admin
from blog.models import blog, contenido


# Register your models here.



class blogadmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')




admin.site.register(blog,blogadmin )
admin.site.register(contenido)

