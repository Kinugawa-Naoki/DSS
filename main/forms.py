from django import forms
from django.urls import timezone

class CreateDeliverableInfo(forms.Form):
    name = forms.CharField(max_length=100, label='成果物名')
    git_url = forms.URLField(label='Git URL')
    category = forms.CharField(max_length=100, label='カテゴリー')
    languages = forms.CharField(max_length=50, label='使用言語')
    option = forms.CharField(max_length=100, null=True, blank=True, label='追記情報')