from django import forms

class SignupForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary', 'name':'user_id'}),
        required=True,
        label='ユーザーID '
    )
    user_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'user_pass'}),
        required=True,
        label='パスワード '
    )
    agree_terms = forms.BooleanField(
        required=True
    )

class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary', 'name':'user_id'}),
        required=True,
        label='ユーザーID '
    )
    user_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'user_pass'}),
        required=True,
        label='パスワード '
    )
