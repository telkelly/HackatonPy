from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterUserForm, UserProfileUpdateForm, ProfileUpdateForm
from .models import Profile


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'  # Specify your login template

    def form_valid(self, form):
        # Custom logic after successful login
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Custom logic for invalid login
        messages.error(self.request, 'There is a problem with login. Check your username or password.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class MyLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been logged out')
        return super().dispatch(request, *args, **kwargs)


def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Registration was successful')
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'accounts/signup.html', {'form':form})


def profile(request, user_id):
    user = get_object_or_404(User, pk = user_id)

    return render(request, 'accounts/profile.html', {'user':user})


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
        'form':form
    })


@login_required
@login_required
def update_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile', user_id=user.id)
    else:
        user_form = UserProfileUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/update_profile.html', context)