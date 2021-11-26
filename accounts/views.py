from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def loginPage(request):
    # login_form = UserLoginForm()
    # context = {'form':login_form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            # return render(request,'accounts/login.html')

    return render(request,'accounts/login.html')


def registerPage (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request,'success messsage')
                return redirect('home')
            return redirect('login')
    
    form = RegistrationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
            
    context = {'user_form':user_form,'profile_form':profile_form}

    return render(request, 'accounts/profile.html',context)

def user_account_detail(request,pk):
    user = User.objects.get(pk=pk)
    context = {"user":user}
    return render(request, 'accounts/user_account_detail.html',context)