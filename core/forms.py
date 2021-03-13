from django import forms
from django.db import models
from django.db.models import fields
from .models import ContactUsModel, NewsLetterModel


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = ('email', 'phone')


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ('fullname', 'title', 'description') 