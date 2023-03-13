from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


def user_have_profile(required=True, is_super_user=False, get=True):
    def get_profile_f(function):
        def finished_function(request, *args, **kwargs):
            profile = None
            try:
                profile = request.user.profile
                if is_super_user:
                    if not profile.user.is_superuser:
                        return HttpResponse('Недостаточно прав')
            except:
                if required:
                    # return None
                    return HttpResponseRedirect(reverse('account:user_login'))
            if get:
                return function(request, profile=profile, *args, **kwargs)
            else:
                return function(request, *args, **kwargs)
        return finished_function
    return get_profile_f


def get_profile_executor(required=True):
    def get_profile_f(function):
        def finished_function(request, profile=None, *args, **kwargs):
            profile_executor = None
            try:
                profile_executor = request.user.profile.profile_executor
            except:
                if required:
                    return HttpResponseRedirect(reverse('start:error'))
                else:
                    profile_executor = None
            return function(request, profile=profile, profile_executor=profile_executor, *args, **kwargs)
        return finished_function
    return get_profile_f
