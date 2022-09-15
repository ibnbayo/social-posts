from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            form.save()
            messages.success(request, f"{username}, account created successfully")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'my_app/signup.html', {'form': form})