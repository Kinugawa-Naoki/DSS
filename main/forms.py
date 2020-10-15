from django import forms
from datetime import datetime

from django.forms.widgets import CheckboxInput

class SignupLoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'', 'name':'user_id'}),
        required=True
    )
    user_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'', 'name':'user_pass'}),
        required=True
    )

class CreateDeliverableInfo(forms.Form):
    user_id_str = ''
    user_id = forms.CharField(
        widget=forms.HiddenInput(attrs={'value':user_id_str})
    )
    name = forms.CharField(
        max_length=100,
        label='成果物名',
        required=True
    )
    git_url = forms.URLField(
        label='Git URL',
        required=True
    )
    category = forms.CharField(
        max_length=100,
        label='カテゴリー',
        required=True
    )
    LANGUAGE_CHOICE = (
        ('C', 'C/C++'),
        ('py3','python3'),
        ('JS','JavaScript'),
        ('SQL','SQL'),
        ('C#','C#'),
        ('Java','Java'),
        ('VBA','VBA'),
        ('HTML/CSS','HTML/CSS')
    )
    languages = forms.ChoiceField(
        choices=LANGUAGE_CHOICE,
        label='使用言語',
        required=True,
        widget=forms.CheckboxInput(check_test=True)
    )
    option = forms.CharField(
        max_length=100,
        label='追記情報'
    )
    now_datetime = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M-%S')
    created_at = forms.DateTimeField(
        widget=forms.HiddenInput(attrs={'value':now_datetime})
    )