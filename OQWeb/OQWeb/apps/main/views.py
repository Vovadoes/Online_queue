from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

def main_page(request):
    return render(request, 'main/Main_page.html', {})