from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.

def home_screen_view (request):
    context = {}
    blog_posts = sorted(BlogPost.objects.all(), key=lambda x: x.date_updated, reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)
