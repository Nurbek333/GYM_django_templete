from django.forms import ModelForm
from .models import Contact
from django import forms
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","phone_number","description"]


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Maqola matnini kiriting'}))
    image = forms.ImageField()

class CommentForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)
    # rating = forms.IntegerField(validators=[MinValueValidator(1),]) 