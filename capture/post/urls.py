from django.urls import path
from . import views
from .views import PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static


# app routes

urlpatterns = [
    path('', PostListView.as_view(), name='capture-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', views.post, name='capture-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)