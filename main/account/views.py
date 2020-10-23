from django.http import request
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# サインアップ
def signupfunc(request):
    forms = SignupForm()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        if len(user_id) > 20:
            return render(request, 'signup.html', {'ID_error':'ユーザーIDは20文字以下にして下さい', 'forms':forms})
        try:
            User.objects.get(username=user_id)
            return render(request, 'signup.html', {'ID_Error':'このユーザーIDでは登録できません', 'forms':forms})
        except:
            User.objects.create_user(user_id, '', user_pass)
            return render(request, 'process_success.html', {'message':'ユーザー登録'})
    else:
        return render(request, 'signup.html', {'forms':forms})

# 利用規約
def termsfunc(request):
    return render(request, 'terms.html', {'terms':''})

# ログイン画面
def loginfunc(request):
    forms = LoginForm()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user = authenticate(username=user_id, password=user_pass)
        # ユーザーが存在するか確認する
        if user is not None:
            login(request, user)
            return redirect('deliverable_list')
        else:
            return render(request, 'login.html', {'error_message':'ログインに失敗しました。', 'forms':forms})
    else:
        return render(request, 'login.html', {'forms':forms})

@login_required
# ログアウト
def logoutfunc(request):
    logout(request)
    return render(request, 'process_success.html', {'message':'ログアウト'})