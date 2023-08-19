from django import forms

from users.forms import StyleFormMixin
from users.models import Users
from .models import Distribution, Message


class DistributionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ('time', 'frequency', 'status', 'message')


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body')
