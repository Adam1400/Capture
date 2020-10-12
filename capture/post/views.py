from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse




# temporary dummy data
posts = [
    {
        'user': 'adam1400',
        'comment': 'Testing database... works localy. Does not work on heroku YET. Striggling to get staic files hosted on heroko. This includes css and in this case database migrations.',
        'content': 'https://arts.unco.edu/images/music/campus-commons/CCPH_Interior_1200x800.jpg',
        'post_date': 'September 28, 2020'    
    },
    {
        'user': 'adam1400',
        'comment': 'testing test 1, comments would go here',
        'content': 'https://pbs.twimg.com/media/DeDR1NgW0AEgDJq.jpg',
        'post_date': 'September 19, 2020'
    },
    {
        'user': 'adam1400',
        'comment': 'second post test 2, comments would go here',
        'content': 'https://patch.com/img/cdn20/users/22137850/20200907/043945/styles/patch_image/public/screen-shot-2020-09-07-at-10627-pm___07163411370.png?width=695',
        'post_date': 'September 9, 2020'       
    }   
]


# load templates
def index(request):
    # this is not working on heroku
    context = { 'posts': Post.objects.all() }
    #context = { 'posts': posts }
    return render(request, 'post/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date'] # order of posts (newest first)

def post(request):
    
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        
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


    


