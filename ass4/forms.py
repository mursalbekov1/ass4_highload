from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ass4.models import SecureData


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SecureDataForm(forms.ModelForm):
    class Meta:
        model = SecureData
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if "<" in name or ">" in name:  # Простая защита от XSS
            raise forms.ValidationError("Недопустимые символы в имени.")
        return name