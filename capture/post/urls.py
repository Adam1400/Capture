from django.urls import path
from . import views
from .views import PostListView, PostDetailView


# app routes

urlpatterns = [
    path('', PostListView.as_view(), name='capture-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', views.post, name='capture-post')
]
