from django.shortcuts import render
from .models import Blog,Tag
from .forms import BlogForm
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    context = {'blogs':blogs,'tags':tags}
    return render(request, 'blog/home.html',context)

def blogs(request):
    blogs = Blog.objects.all()
    # for blog in blogs:
    #     blog['tags'] = blog.tags.all()
    tags = Tag.objects.all()
    context = {'blogs':blogs,'all_tags':tags}
    return render(request, 'blog/blogs.html', context)

def read_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    tags = blog.tags.all()
    all_tags = Tag.objects.all()
    context = {'blog':blog,'tags':tags,'all_tags':all_tags}
    return render(request, 'blog/blog_detail.html',context)

def add_blog(request):
    form = BlogForm(),n,
    context = {'form':form}
    return render(request, 'blog/blog_add.html', context)
def about(request):
    return render(request, 'blog/about.html')