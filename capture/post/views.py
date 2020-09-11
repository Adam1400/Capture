from django.shortcuts import render
from django.http import HttpResponse

# test posts
posts = [
    {
        'user': 'Test_user_1',
        'comment': 'testing test 1, comments would go here',
        'content': 'https://pbs.twimg.com/media/DeDR1NgW0AEgDJq.jpg',
        'post_date': 'September 9, 2020'
    },
    {
        'user': 'Test_user_2',
        'comment': 'second post test 2, comments would go here',
        'content': 'https://patch.com/img/cdn20/users/22137850/20200907/043945/styles/patch_image/public/screen-shot-2020-09-07-at-10627-pm___07163411370.png?width=695',
        'post_date': 'September 19, 2020'
    }
]

# load templates
def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context)

def post(request):
    return render(request, 'post/post.html', {'title': 'Post'})
