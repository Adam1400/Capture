from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from users.models import Profile
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from django.contrib import messages


# load templates
class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date'] # order of posts (newest first)


@login_required
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True


    
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class PostDetailView(DetailView, DeleteView):
    model = Post
    template_name = 'post/post_detail.html'
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        thisPost = get_object_or_404(Post, id=self.kwargs['pk'])

        postLikes = thisPost.likes.all()
        

        liked = False
        if thisPost.likes.filter(id=self.request.user.id).exists():
            liked= True
        
        context.update({
            'liked': liked,
            'postLikes': postLikes
        })
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


@login_required  
def post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        form.instance.user = request.user
        form.post_date = timezone.localtime(timezone.now())

        if form.is_valid():
            form.save()
            indexcontext = { 'posts': Post.objects.all() }
            return HttpResponseRedirect(reverse('capture-home'))

    
    context = {'form':form, 'title': 'Post'}
    return render(request, 'post/post.html', context )

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['comment', 'content']

        
        
            
    


