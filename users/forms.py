from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import Users


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UsersRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'avatar', 'email', 'password1', 'password2')


class UsersForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = Users
        fields = ('email', 'password', 'avatar', 'first_name', 'last_name', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
