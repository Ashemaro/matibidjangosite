from django import forms
from .models import ContactMessage, News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  # Ensure email is saved
        if commit:
            user.save()
            messages.success(self.request, "Registration successful. You can now log in.")
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class NewsForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('News', 'News'),
        ('NookHubActivities', 'NookHubActivities'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')  # Add category field

    class Meta:
        model = News
        fields = ['title', 'slug', 'author', 'category', 'content', 'status', 'image']  # Add category field to the form