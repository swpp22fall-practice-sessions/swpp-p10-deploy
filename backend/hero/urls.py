from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('info/', views.hero_list, name='hero_list'),
    path('info/<int:id>/', views.hero_info, name='hero_info')
]
