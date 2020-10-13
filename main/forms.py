from django import forms
from django.urls import timezone

class CreateDeliverableInfo(forms.Form):
    name = forms.CharField(max_length=100)
    git_url = forms.URLField()
    category = forms.CharField(max_length=100)
    languages = forms.CharField(max_length=50)
    option = forms.CharField(max_length=100, null=True, blank=True)
    created_dt = forms.DateTimeField(default=timezone.now)
    modified_dt = forms.DateTimeField(null=True, blank=True)