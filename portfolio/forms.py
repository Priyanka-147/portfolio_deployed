from django import forms
from .models import (
    NavbarLink, Hero, About, SocialLink,
    Project, SkillCategory, Skill,
    ContactInfo, Message, FooterLink
)

class ContactForm(forms.ModelForm):
    """Form for contact messages"""
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message',
                'rows': 5
            })
        }

class ProjectForm(forms.ModelForm):
    """Form for project management"""
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'image',
            'skills1', 'skills2', 'skills3', 'skills4',
            'code_link', 'demo_link'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'skills1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Frontend Skills (comma-separated)'
            }),
            'skills2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Backend Skills (comma-separated)'
            }),
            'skills3': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Database Skills (comma-separated)'
            }),
            'skills4': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Other Skills (comma-separated)'
            }),
            'code_link': forms.URLInput(attrs={'class': 'form-control'}),
            'demo_link': forms.URLInput(attrs={'class': 'form-control'})
        }

class AboutForm(forms.ModelForm):
    """Form for about section"""
    class Meta:
        model = About
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            })
        }

class SkillCategoryForm(forms.ModelForm):
    """Form for skill categories"""
    class Meta:
        model = SkillCategory
        fields = ['name', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class SkillForm(forms.ModelForm):
    """Form for individual skills"""
    class Meta:
        model = Skill
        fields = ['category', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

class SocialLinkForm(forms.ModelForm):
    """Form for social media links"""
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'icon']
        widgets = {
            'platform': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., LinkedIn, GitHub'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://'
            })
        }

class ContactInfoForm(forms.ModelForm):
    """Form for contact information"""
    class Meta:
        model = ContactInfo
        fields = ['email', 'phone', 'location']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (123) 456-7890'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, Country'
            })
        }

class NavbarLinkForm(forms.ModelForm):
    """Form for navbar links"""
    class Meta:
        model = NavbarLink
        fields = ['name', 'url', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Link Name'
            }),
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/path or https://'
            })
        }

class FooterLinkForm(forms.ModelForm):
    """Form for footer links"""
    class Meta:
        model = FooterLink
        fields = ['name', 'url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Link Name'
            }),
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/path or https://'
            })
        }
