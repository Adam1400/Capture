from django.urls import path
from . import views
from .views import PostListView


# app routes

urlpatterns = [
    # not working on heroku
    # path('', PostListView.as_view(), name='capture-home'),
    path('', views.index, name='capture-home'),
    path('post/', views.post, name='capture-post'),
]