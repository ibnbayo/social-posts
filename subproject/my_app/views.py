
from django.shortcuts import render, redirect

from .forms import SignUpForm, CreatePostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_home_page(request):
    posts = Post.objects.all()[:1]
    print(posts)
    return render(request, 'my_app/home.html', {'posts': posts})

def get_about_page(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'my_app/about.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            form.save()
            messages.success(request, f"{username}, account created successfully")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'my_app/signup.html', {'form': form})

def sides(request):
    posts = Post.objects.all()
    last_post = Post.objects.all().last()
    print(posts)
    return render(request, 'my_app/sides.html', {'posts': posts,'last_post': last_post})

@login_required
def createpost(request):
    user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data.get('title')
            form_body = form.cleaned_data.get('body')
            Post.objects.create(title=form_title, body=form_body, owner=user)
            messages.success(request, "Post created successfully")
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'my_app/createpost.html', {'form': form})
   