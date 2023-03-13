from django import forms
# from django.contrib.auth.models import User
from django.forms import widgets
from .models import Queue

class QueueForm(forms.ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"required placeholder":"Пароль", 'class': 'field'}))
    # password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"required placeholder":"Повторите пароль", 'class': 'field'}))

    class Meta:
        model = Queue
        fields = ('parallelization', 'waiting_time_max')
        widgets={
            'parallelization': forms.TextInput(attrs={"required placeholder":"Логин", 'class': 'field'}),
            'waiting_time_max': forms.TextInput(attrs={"required placeholder":"Имя", 'class': 'field'})
        }
