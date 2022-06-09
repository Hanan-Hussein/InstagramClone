from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm, ImageForm, ProfileEditForm,CommentsForm
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image, Profile, Followers, Like, Comments
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def home(request):
    posts = Image.objects.all()
    user_display = request.user
    users = User.objects.all()
    users = User.objects.all().exclude(id=request.user.id)
    followers_posts = Image.objects.all()
    followed = [i for i in User.objects.all() if Followers.objects.filter(
        followers=request.user, followed=i)]
    if followed:
        for i in followed:

            followers_posts = Image.objects.all().filter(user=i).order_by('pub_date')

            followers_posts = Image.objects.all()
    else:
        followers_posts = Image.objects.all().filter(
            user=request.user).order_by('pub_date')

    return render(request, 'home.html', {"posts": posts, "user_display": user_display, "users": users, "followed": followed, "followers_posts": followers_posts},)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful, Please Login")
            return redirect("login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, template_name="auth/register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'auth/login.html', context=context)

@login_required
def explore(request):
    posts = Image.objects.all()
    user_display = request.user
    return render(request, 'explore.html', {"posts": posts, "user_display": user_display})
@login_required
def image_upload(request):
    user_display = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            caption = form.cleaned_data['caption']

            form = Image(name=name, image=image, caption=caption,
                         user=request.user)
            form.save()
            messages.success(request, "Post created successful")
            return redirect('home')
    form = ImageForm()

    context = {
        "form": form,
        "user_display": user_display
    }
    return render(request, 'upload.html', context=context)
def logout_request(request):
    logout(request)
    return redirect('login')
