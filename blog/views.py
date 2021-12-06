from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Blog, Category, Comment,Tag, Like,Bookmark
from .forms import BlogForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    context = {'blogs':blogs,'tags':tags}
    return render(request, 'blog/home.html',context)

def blogs(request, tag='all'):
    if tag == 'all': 
        blogs = Blog.objects.all()
    else:
        t = Tag.objects.get(name=tag)
        blogs = t.blog_set.all()
        # blogs = Blog.objects.filter(tags=t)
    search_query = request.GET.get("search")
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)
    
    catagories = Category.objects.all()
    tags = Tag.objects.all()
    latest_blogs = Blog.objects.all().order_by('-updated_at')[:5]
    context = {
        'blogs':blogs,'all_tags':tags,'catagories':catagories,
        'latest_blogs':latest_blogs,
        }
    return render(request, 'blog/blogs.html', context)

def read_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    likes = Like.objects.filter(blog=blog)
    if request.user.is_authenticated:
        is_liked_by_user = likes.filter(user=request.user).exists()
    else:
        is_liked_by_user = False 
    comments = Comment.objects.filter(blog=blog)
    catagories = Category.objects.all()
    latest_blogs = Blog.objects.all().order_by('-updated_at')[:5]
    tags = blog.tags.all()
    all_tags = Tag.objects.all()
    context = {
        'blog':blog,'tags':tags,'all_tags':all_tags,
        'likes':likes, 'comments':comments,'catagories':catagories,
        'is_liked_by_user':is_liked_by_user,
        'latest_blogs':latest_blogs
        }
    return render(request, 'blog/blog_detail.html',context)


@login_required
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            return redirect('read-blog',blog.id)
        #     print("********* Form is Valid *********")
    context = {'form':form}
    return render(request, 'blog/blog_create.html', context)

def about(request):
    return render(request, 'blog/about.html')


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        user = request.user
        body = request.POST.get('body')
        comment = Comment(body=body, user=user,blog=blog)
        # print(comment)
        comment.save()
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)
    
    return redirect('home')

@login_required
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

@login_required
def auth_user_blog(request):
    user = request.user
    blogs = Blog.objects.filter(author= user)
    #  likes = Like.objects.filter(blog=blog)
    # comments = Comment.objects.filter(blog=blog)
    tags = Tag.objects.all()
    context = {'blogs':blogs,'all_tags':tags}
    return render(request, 'blog/blogs.html', context)


@login_required
def auth_user_bookmark(request):
    user = request.user
    # bookmarks = Bookmark.objects.filter(user= user)
    blogs = Blog.objects.filter()
    catagories = Category.objects.all()
    tags = Tag.objects.all()
    latest_blogs = Blog.objects.all().order_by('-updated_at')[:5]
    # bookmark = Bookmark.objects.filter(user=request.user)
    # bookmark = Blog.objects.filter(bookmark__user=user)
    bookmark = Blog.objects.filter(bookmark__user=user)
    context = {
        'blogs':blogs,'all_tags':tags,'catagories':catagories,
        'latest_blogs':latest_blogs,'bookmarks':bookmark
        }
    return render(request, 'blog/blog_bookmark.html', context)
    # return redirect('home')

@login_required
def like_blog(request,pk):
    blog = Blog.objects.get(pk = pk)
    like = Like.objects.create(user=request.user, blog=blog, liked=True)
    return redirect('read-blog',pk)


@login_required
def bookmark(request,pk):
    user = request.user
    blog = Blog.objects.get(pk=pk)
    bookmark = Bookmark.objects.get(user=user)
    if bookmark:
        bookmark.blog.add(blog)
    else:
        new_bookmark = Bookmark.objects.create(user=user)
        new_bookmark.blog.add(new_bookmark)
        new_bookmark.save()
    return redirect('read-blog',pk)

def search(request):
    q = request.GET.get('search')
    print('###'*40)
    blog = Blog.objects.filter(title__icontains=q)
    print(blog)
    return redirect('home')
