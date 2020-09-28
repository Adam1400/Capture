from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post





# load templates
def index(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'post/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date'] # order of posts (newest first)

def post(request):
    return render(request, 'post/post.html', {'title': 'Post'})
