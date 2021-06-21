
from django import forms

from website.FunLearning.models import user


class UserForm(forms.ModelForm):
    class Meta:
        model = user
        widgets = {
        'password': forms.PasswordInput(),
    }
        nvjfhvhjbhjvj
