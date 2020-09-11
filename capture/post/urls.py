from django.urls import path
from . import views

# app routes

urlpatterns = [
    path('', views.index, name='capture-home'),
    path('post/', views.post, name='capture-post'),
]