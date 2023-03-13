from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.user_login, name = 'user_login'),
    path('profile/', views.profile, name = 'profile'),
    path('groups/', views.groups, name = 'groups'),
]