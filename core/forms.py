from django import forms
from django.db.models import fields
from .models import AboutUsModel

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUsModel
        fields = '__all__'