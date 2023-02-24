from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('proceso', views.proceso, name='proceso'),
    path('Bienvenida', views.bienvenida, name='bienvenida'),
    path('Suma', views.suma, name='suma'),
    path('Resta', views.resta, name='resta'),
    path('Multiplicacion', views.multiplicacion, name='multiplicacion'),
    path('Division', views.division, name='division'),
]