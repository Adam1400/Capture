from django.urls import path
from . import views
from .views import PostListView


# app routes

urlpatterns = [
    path('', PostListView.as_view(), name='capture-home'),
    path('post/', views.post, name='capture-post'),
]