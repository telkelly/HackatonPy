from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from .forms import RegisterUserForm, UserProfileUpdateForm


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There is a problem with login, check your username or password.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.error(request, 'You were logged out')
    return redirect('home')


def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration was successful')
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'accounts/signup.html', {'form': form})


def profile(request, user_id):
    user = get_object_or_404(User, pk = user_id)

    return render(request, 'accounts/profile.html', {'user': user})


def update_profile(request, user_id):
    user = User.objects.get(pk = user_id)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return render(request, 'accounts/profile.html', {'user': user})
    else:
        form = UserProfileUpdateForm(instance=user)

    return render(request, 'accounts/update_profile.html', {'form': form})


def update_password(request, user_id):
    user = User.objects.get(pk = user_id)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            userForm = form.save()
            update_session_auth_hash(request, userForm)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })