from django import forms
from datetime import datetime

class SignupLoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'', 'name':'user_id'}),
        required=True,
        label='ユーザーID'
    )
    user_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'', 'name':'user_pass'}),
        required=True,
        label='パスワード'
    )

class CreateDeliverableInfo(forms.Form):
    deliverable_name = forms.CharField(
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
    lang_choice = [
        ('C/C++', 'C/C++'),
        ('python3','python3'),
        ('JavaScript','JavaScript'),
        ('SQL','SQL'),
        ('C#','C#'),
        ('Java','Java'),
        ('VBA','VBA'),
        ('HTML/CSS','HTML/CSS')
    ]
    languages = forms.MultipleChoiceField(
        label='使用言語',
        widget=forms.CheckboxSelectMultiple(),
        choices=lang_choice,
        required=True
    )
    own_comment = forms.CharField(
        max_length=100,
        label='追記情報',
        required=False
    )