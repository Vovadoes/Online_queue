from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Group
from account.models import Profile


def get_group(required=True, get=True):
    def get_group_f(function):
        def finished_function(request, group_id, *args, **kwargs):
            group = None
            group = Group.objects.filter(id=group_id)
            if required:
                if len(group) == 0:
                    return HttpResponseRedirect(reverse('main:main'))
            if len(group) > 0:
                group = list(group)[-1]
            if get:
                return function(request, group=group, *args, **kwargs)
            else:
                return function(request, *args, **kwargs)
        return finished_function
    return get_group_f


def user_in_group(required=True, get=True):
    def get_group_f(function):
        def finished_function(request, profile: Profile, group: Group, *args, **kwargs):
            # try:
            groups_profile: list[Group] = Group.objects.filter(
                profils=profile.id)
            groups_admin: list[Group] = Group.objects.filter(
                admins=profile.id)
            print([[j for j in i.profils] for i in groups_profile])
            # except:
            #     if required:
            #         # return None
            #         return HttpResponseRedirect(reverse('main:main'))
            if get:
                return function(
                    request=request, profile=profile, group=group,
                    groups_profile=groups_profile, groups_admin=groups_admin,
                    *args, **kwargs
                )
            else:
                return function(request=request, profile=profile, group=group, *args, **kwargs)
        return finished_function
    return get_group_f


def user_is_admin_group(required=True, get=True):
    def get_group_f(function):
        def finished_function(request, profile, *args, **kwargs):
            profile = None
            try:
                profile = request.user.profile
            except:
                if required:
                    # return None
                    return HttpResponseRedirect(reverse('main:main'))
            if get:
                return function(request, profile, *args, **kwargs)
            else:
                return function(request, *args, **kwargs)
        return finished_function
    return get_group_f
