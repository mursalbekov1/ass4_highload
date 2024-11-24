from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailForm(forms.Form):
    recipient = forms.EmailField(label="Получатель", required=True)
    subject = forms.CharField(label="Тема", max_length=255, required=True)
    body = forms.CharField(label="Текст сообщения", widget=forms.Textarea, required=True)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
