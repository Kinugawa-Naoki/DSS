from django import forms
from datetime import datetime

class CreateDeliverableInfo(forms.Form):
    deliverable_name = forms.CharField(
        label='成果物名',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True,
    )
    git_url = forms.URLField(
        label='Git URL',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True,
    )
    category = forms.CharField(
        label='カテゴリー',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True,
    )
    lang_choice = [
        ('C/C++', 'C/C++'),
        ('Python3','Python3'),
        ('JavaScript','JavaScript'),
        ('SQL','SQL'),
        ('C#','C#'),
        ('Java','Java'),
        ('VBA','VBA'),
        ('HTML/CSS','HTML/CSS'),
        ('その他','その他')
    ]
    languages = forms.MultipleChoiceField(
        label='使用言語',
        widget=forms.CheckboxSelectMultiple(),
        choices=lang_choice,
        required=True,
    )
    own_comment = forms.CharField(
        label='追記情報',
        widget=forms.Textarea(attrs={'class':'form-control'}),
        max_length=100,
        required=False,
    )
    non_display = forms.BooleanField(
        label='チェックを入れると他の人には公開されません',
        required=False,
    )

# 評価コメント
class Comment(forms.Form):
    comment = forms.CharField(
        label='コメント投稿欄',
        widget=forms.Textarea(attrs={'class':'form-control'}),
        max_length=500,
        required=True
    )