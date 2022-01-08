
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from formula1app.views import inicio
from formula1app import views 


urlpatterns = [
    path('', views.inicio, name="inicio"),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



