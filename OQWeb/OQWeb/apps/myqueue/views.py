from django.shortcuts import render
from account.decorators import user_have_profile
from account.models import Profile
from .forms import QueueForm
from .decorators import *
from django.http import Http404, HttpResponseRedirect, HttpResponse


@user_have_profile()
@get_group(required=False)
@user_in_group()
def group(request, profile: Profile, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('')


@user_have_profile()
def create_queue(request, profile: Profile, *args, **kwargs):
    if request.method == "POST":
        queue_form = QueueForm(request.POST)
        if queue_form.is_valid():
            return render(request, "myqueue/create_queue.html", {'queue_form': queue_form})
        else:
            return render(request, "myqueue/create_queue.html", {'queue_form': queue_form})
    else:
        queue_form = QueueForm()
        return render(request, "myqueue/create_queue.html", {'queue_form': queue_form})
