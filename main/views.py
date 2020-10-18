from django.core.checks import messages
from django.db import models
from django.shortcuts import redirect, render
from .forms import CreateDeliverableInfo, SignupLoginForm
from .models import DeliverableInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create

# サインアップ
def signupfunc(request):
    forms = SignupLoginForm()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        if len(user_id) > 100:
            return render(request, 'signup.html', {'error':'ユーザーIDは100文字以下にして下さい'})
        try:
            User.objects.get(username=user_id)
            return render(request, 'signup.html', {'error':'このユーザーIDでは登録できません', 'form':forms})
        except:
            User.objects.create_user(user_id, '', user_pass)
            return render(request, 'login.html', {'message':'ユーザー登録が完了しました', 'form':forms})
    else:
        print(forms)
        return render(request, 'signup.html', {'forms':forms})

# ログイン画面
def loginfunc(request):
    forms = SignupLoginForm()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user = authenticate(username=user_id, password=user_pass)
        # ユーザーが存在するか確認する
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error':'ログインに失敗しました。', 'forms':forms})
    else:
        return render(request, 'login.html', {'forms':forms})

# ここからログインが必要
@login_required

# ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')

# 成果物情報登録
def createfunc(request):
    form = CreateDeliverableInfo()
    if request.method == 'POST':
        user_id = request.user
        deliverable_name = request.POST['deliverable_name']
        git_url = request.POST['git_url']
        category = request.POST['category']
        languages = request.POST['languages']
        own_comment = request.POST['own_comment']
        created_dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        models = DeliverableInfo(
            user_id = user_id,
            deliverable_name = deliverable_name,
            git_url = git_url,
            category = category,
            languages = languages,
            own_comment = own_comment,
            created_dt = created_dt
        )
        models.save()
        return render(request, 'deliverable_list.html', {'message':'登録が完了しました。'})
    else:
        return render(request, 'create_deliverable_info.html', {'forms':form})

# 投稿した成果物「一覧のリスト」を見る
def deliverable_listfunc(request):
    user_id = request.user
    list_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).all()
    return render(request, 'deliverable_list.html', {'list_query':list_query})

# 投稿した成果物を見る
def deliverable_detailfunc(request, pk):
    username = request.user
    detail_query = DeliverableInfo.objects.filter(user_id__iexact=username).get(pk=pk)
    return render(request, 'deliverable_detail.html', {'detail_query':detail_query})