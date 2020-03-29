from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from . import views 
  
urlpatterns = [ 
    path('', views.index ),
    path('stats/', views.show_stats),
    path('supplies/', views.show_supplies),
]