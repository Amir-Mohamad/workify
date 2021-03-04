from django import forms
from django.db import models
from django.db.models import fields
from .models import ContactUsModel, NewsLetterModel


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = '__all__'


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = '__all__'