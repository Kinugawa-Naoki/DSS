from django import forms
from datetime import datetime

class CreateDeliverableInfo(forms.Form):
    deliverable_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        label='成果物名 ',
        required=True
    )
    git_url = forms.URLField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Git URL ',
        required=True
    )
    category = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        label='カテゴリー ',
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
        ('HTML/CSS','HTML/CSS'),
        ('その他','その他')
    ]
    languages = forms.MultipleChoiceField(
        label='使用言語 ',
        widget=forms.CheckboxSelectMultiple(),
        choices=lang_choice,
        required=True
    )
    own_comment = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}),
        max_length=100,
        label='追記情報 ',
        required=False
    )