from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)


def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)
