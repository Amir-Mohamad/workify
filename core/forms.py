from django import forms
from django.db.models import fields
from .models import NewsLetterModel


class NewsLetterForm(forms.Form):
    class Meta:
        model = NewsLetterModel
        fields = '__all__'
