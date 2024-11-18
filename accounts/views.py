from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import translation

from Lab2 import settings
from .forms import EmailLoginForm, UserCreationForm, UserProfileForm
from .models import UserProfile, CustomUser


def login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            if user.current_profile is not None:
                translation.activate(user.current_profile.language)
                request.session[settings.LANGUAGE_SESSION_KEY] = user.current_profile.language
            else:
                translation.activate(user.language)
                request.session[settings.LANGUAGE_SESSION_KEY] = user.language
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = EmailLoginForm()

    return render(request, '../templates/pages-login.html', {'form': form})


def create_account_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request=request, template_name="../templates/pages-register.html", context={'form': form})


@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, user=request.user)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.language = request.user.language
            user_profile.save()
            if request.user.current_profile is None:
                request.user.current_profile = user_profile
                request.user.save()
            messages.success(request, "User profile created successfully!")
            return redirect('dashboard')
    else:
        form = UserProfileForm(user=request.user)

    return render(request, '../templates/block-createprofile.html',
                  {'form': form, 'user_profiles': UserProfile.objects.filter(user=request.user)})


@login_required
def switch_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)

    request.user.current_profile = profile
    request.user.save()
    translation.activate(profile.language)
    request.session[settings.LANGUAGE_SESSION_KEY] = profile.language

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


def change_language(request, language_code):
    print(CustomUser.LANGUAGE_CHOICE)
    if language_code not in dict(CustomUser.LANGUAGE_CHOICE):
        return redirect('dashboard')

    if request.user.is_authenticated:
        if request.user.current_profile is not None:
            request.user.current_profile.language = language_code
            request.user.current_profile.save()
        else:
            request.user.language = language_code
            request.user.save()

    translation.activate('es')
    request.session[settings.LANGUAGE_SESSION_KEY] = language_code
    print(request.session[settings.LANGUAGE_SESSION_KEY])
    print(translation.get_language())

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
