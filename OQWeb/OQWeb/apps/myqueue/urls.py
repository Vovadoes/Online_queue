from django.urls import path
from . import views

app_name = 'myqueue'
urlpatterns = [
    path('create/', views.create_queue, name = 'create_queue'),
    path('group/<int:group_id>/', views.group, name = 'group')
]