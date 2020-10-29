from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import deactivate
from .forms import Comment, CreateDeliverableInfo
from .models import DeliverableInfo, PablicComment
from datetime import datetime

# メインページ
def indexfunc(request):
    list_query = DeliverableInfo.objects.filter(non_display__iexact=None).all()
    return render(request, 'index.html', {'list_query':list_query})

# 成果物の詳細情報を見る
def deliverable_detailfunc(request, pk):
    form = Comment()
    if request.method == 'POST':
        comment_model = PablicComment(
            deliverable_id = DeliverableInfo.objects.get(pk=pk),
            post_user_id = request.user,
            comment = request.POST['comment']
        )
        comment_model.save()
        redirect_path = '/deliverable_detail/' + str(pk)
        return redirect(redirect_path)
    else:
        try:
            detail_query = DeliverableInfo.objects.get(id=pk)
            comment_query = PablicComment.objects.filter(deliverable_id__id__iexact=pk).all()
            return render(request, 'deliverable_detail.html', {'detail_query':detail_query, 'comment_query':comment_query, 'comment_form':form})
        except:
            return redirect('deliverable_detail')


# ここからログインが必要
# 成果物情報登録
@login_required
def createfunc(request):
    form = CreateDeliverableInfo()
    if request.method == 'POST':
        # 使用言語取り出し
        languages_list = request.POST.getlist('languages')
        languages = ''
        for language in languages_list:
            languages = languages + language + ', '
        if languages == '':
            return render(request, 'create_deliverable_info.html', {'forms':form, 'message':'どれか一つを必ず選択してください。'})
        # 新規登録
        models = DeliverableInfo(
            user_id = request.user,
            deliverable_name = request.POST['deliverable_name'],
            git_url = request.POST['git_url'],
            category = request.POST['category'],
            languages = languages,
            own_comment = request.POST['own_comment'],
            created_dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
            non_display = request.POST.get('non_display')
        )
        print(request.POST)
        models.save()
        return render(request, 'process_success.html', {'message':'作成'})
    else:
        return render(request, 'create_deliverable_info.html', {'forms':form})

# 成果物の一覧リストを見る
def deliverable_listfunc(request):
    user_id = request.user()
    list_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).all()
    list_query_counter = DeliverableInfo.objects.filter(user_id__iexact=user_id).count()
    if list_query_counter == 0:
        list_query = 'None'
    return render(request, 'deliverable_list.html', {'list_query':list_query})

# 成果物を更新する
def deliverable_updatefunc(request, pk):
    user_id = request.user
    if request.method == 'POST':
        # 入力データの引き出し・加工
        languages_list = request.POST.getlist('languages')
        languages = ''
        for language in languages_list:
            languages = languages + language + ', '
        
        #　成果物情報の上書き
        model_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).get(pk=pk)
        model_query.deliverable_name = request.POST['deliverable_name']
        model_query.git_url = request.POST['git_url']
        model_query.category = request.POST['category']
        model_query.languages = languages
        model_query.own_comment = request.POST['own_comment']
        model_query.modified_dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        model_query.save()
        return render(request, 'process_success.html', {'message':'更新'})
    
    else:
        try:
            detail_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).get(pk=pk)
            # 成果物名のみ取り出し
            deliverable_name = detail_query.deliverable_name
            # 登録済みの使用言語取り出し・初期値代入用辞書作成
            lang_list = detail_query.languages.split(', ')
            lang_list.pop()
            initial_dict = {
                'deliverable_name':deliverable_name,
                'git_url':detail_query.git_url,
                'category':detail_query.category,
                'languages':lang_list,
                'own_comment':detail_query.own_comment,
                'non_display':detail_query.non_display,
            }
            form = CreateDeliverableInfo(initial=initial_dict)
            return render(request, 'deliverable_update.html', {'form':form, 'deliverable_name':deliverable_name})
        except:
            return redirect('deliverable_list')

# 成果物を削除する
def deliverable_deletefunc(request, pk):
    user_id = request.user
    if request.method == 'POST':
        model = DeliverableInfo.objects.filter(user_id__iexact=user_id).get(pk=pk)
        delete_name = model.deliverable_name
        model.delete()
        return render(request, 'process_success.html', {'delete_name':delete_name, 'message':'の削除'})
    else:
        try:
            detail_query = DeliverableInfo.objects.filter(user_id__iexact=user_id).get(pk=pk)
            return render(request, 'deliverable_delete.html', {'detail_query':detail_query})
        except:
            return redirect('deliverable_list')


def add_comment(request):
    return 