from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
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

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.cleaned_data.get('cover_image'))
        if form.is_valid():
            blog = form.save()
            return redirect('read-blog',blog.id)
        #     print("********* Form is Valid *********")
    else:
        print("######### Invalid #######\n")
        form = BlogForm()
    context = {'form':form}
    return render(request, 'blog/blog_create.html', context)

def about(request):
    return render(request, 'blog/about.html')


@login_required(login_url='/')
def add_comment(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        user = request.user
        body = request.POST.get('body')
        comment = Comment(body=body, user=user,blog=blog)
        print(comment)
        comment.save()
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)
    else:
        return redirect('home')

def edit_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogForm(instance=blog)
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            blog.save()
            return redirect('read-blog', blog.pk)
    context={'blog':blog,'form':form}
    return render(request, 'blog/blog_edit.html',context)


def auth_user_blog(request):
    user = request.user
    blogs = Blog.objects.filter(author= user)
    #  likes = Like.objects.filter(blog=blog)
    # comments = Comment.objects.filter(blog=blog)
    tags = Tag.objects.all()
    context = {'blogs':blogs,'all_tags':tags}
    return render(request, 'blog/blogs.html', context)
