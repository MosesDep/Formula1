from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from login.views import login
from login import views

urlpatterns = [
    path('', views.login, name="login"),
    

 


]