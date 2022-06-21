from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Aboutme', views.Aboutme, name='Aboutme'),
    path('Aboutstory', views.Aboutstory, name='Aboutstory'),
    path('Map', views.Map, name='Map'),
    path('Story', views.Story, name='Story'),
]