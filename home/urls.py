from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newest', views.newest, name='newest'),
    path('best', views.best, name='best'),

]
