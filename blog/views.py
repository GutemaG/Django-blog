from django.shortcuts import render
from .models import Blog, Category, Comment,Tag, Like
from .forms import BlogForm
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    context = {'blogs':blogs,'tags':tags}
    return render(request, 'blog/home.html',context)

def blogs(request):
    blogs = Blog.objects.all()
    #  likes = Like.objects.filter(blog=blog)
    # comments = Comment.objects.filter(blog=blog)
    tags = Tag.objects.all()
    context = {'blogs':blogs,'all_tags':tags}
    return render(request, 'blog/blogs.html', context)

def read_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    likes = Like.objects.filter(blog=blog)
    comments = Comment.objects.filter(blog=blog)
    catagories = Category.objects.all()
    tags = blog.tags.all()
    all_tags = Tag.objects.all()
    context = {'blog':blog,'tags':tags,'all_tags':all_tags,
        'likes':likes, 'comments':comments,'catagories':catagories}
    return render(request, 'blog/blog_detail.html',context)

def add_blog(request):
    form = BlogForm(),n,
    context = {'form':form}
    return render(request, 'blog/blog_add.html', context)
def about(request):
    return render(request, 'blog/about.html')