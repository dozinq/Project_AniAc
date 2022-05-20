from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm

from django.contrib.auth import authenticate, login as login_process

from django.core.paginator import Paginator
from community.models import Review, Comment

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:main')

    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    #         return redirect('movies:main')
    # else:
    #     form = CustomUserCreationForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'accounts/signup.html', context)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=raw_password, last_name=last_name)  # 사용자 인증
            login_process(request, user, backend='django.contrib.auth.backends.ModelBackend')  # 로그인
            return redirect('movies:main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:main')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:main')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def reviews(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    reviews = Review.objects.filter(user=person).order_by('-pk')
    page        = int(request.GET.get('p', 1))
    paginator   = Paginator(reviews, 10)
    boards      = paginator.get_page(page)

    context = {
        'person': person,
        'boards' : boards,
    }
    return render(request, 'accounts/reviews.html', context)

@login_required
def comments(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    comments = Comment.objects.filter(user=person).order_by('-pk')
    page        = int(request.GET.get('p', 1))
    paginator   = Paginator(comments, 10)
    boards      = paginator.get_page(page)

    context = {
        'person': person,
        'boards' : boards,
    }
    return render(request, 'accounts/comments.html', context)