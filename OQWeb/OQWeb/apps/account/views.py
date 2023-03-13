from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .decorators import user_have_profile
from datetime import datetime
from .models import Profile
from myqueue.models import Group


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('account:profile'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponse('Не все поля заполнены')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print(user_form.is_valid(), profile_form.is_valid())
        print(user_form.errors, profile_form.errors)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_profile: Profile = profile_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # ---
            new_profile.user_id = new_user.id
            new_profile.date_create = datetime.now()
            new_profile.save()
            return render(request, 'account/register_done.html', {'new_user': new_user, 'profile_form': profile_form})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'account/register.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@user_have_profile()
def profile(request, profile,  *args, **kwargs):
    return render(request, 'account/profile.html', {'profile': profile})


@user_have_profile()
def groups(request, profile, *args, **kwargs):
    groups_users = Group.objects.filter(profils=profile)
    groups_admins = Group.objects.filter(admins=profile)
    return render(request, 'account/groups.html',
                  {
                      'profile': profile,
                      "groups_users": groups_users,
                      "groups_admins": groups_admins,
                  }
                  )
