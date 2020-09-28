from django.urls import path
from .views import PostListView
from . import views



# app routes

urlpatterns = [
    path('', PostListView.as_view(), name='capture-home'),
    path('post/', views.post, name='capture-post'),
]