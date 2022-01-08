from django.urls import path
from formula1app import views
from stats import views



urlpatterns = [

    path('', views.stats, name="stats"),
    path('carreras/<nombre>/', views.carreras, name="carreras"),
    path('palmar/<nombre>/', views.palmar, name="palmar"),


]


