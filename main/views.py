from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CreateDeliverableInfo
from .models import DeliverableInfo
from datetime import datetime

# メインページ
def indexfunc(request):
    return render(request, 'index.html', {'somedata':''})


# 処理成功画面
def process_successfunc(request):
    return redirect('login')

# ここからログインが必要
# 成果物情報登録
@login_required
def createfunc(request):
    form = CreateDeliverableInfo()
    if request.method == 'POST':
        user_id = request.user
        deliverable_name = request.POST['deliverable_name']
        git_url = request.POST['git_url']
        category = request.POST['category']
        languages_list = request.POST.getlist('languages')
        languages = ''
        for language in languages_list:
            languages = languages + language + ','
        own_comment = request.POST['own_comment']
        created_dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print(languages)
        if languages == '':
            return render(request, 'create_deliverable_info.html', {'forms':form, 'message':'どれか一つを必ず選択してください。'})
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
        return render(request, 'deliverable_list.html', {'message':'成果物の登録'})
    else:
        return render(request, 'create_deliverable_info.html', {'forms':form})

# 投稿した成果物「一覧のリスト」を見る
@login_required
def deliverable_listfunc(request):
    user_id = request.user
    list_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).all()
    return render(request, 'deliverable_list.html', {'list_query':list_query})

# 投稿した成果物を見る
@login_required
def deliverable_detailfunc(request, pk):
    user_id = request.user
    try:
        detail_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).get(pk=pk)
        return render(request, 'deliverable_detail.html', {'detail_query':detail_query})
    except:
        return redirect('deliverable_list')