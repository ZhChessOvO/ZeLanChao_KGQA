from django.shortcuts import render

from django.contrib import messages
from sqlalchemy import null

from medicine.models import *
from medicine.qs.chatbot_graph import *
import pandas as pd
from medicine.qs.answer_search import *
from medicine.sidefunctions import *
import random


# Create your views here.
def index(request):
    try:
        print(request.session['status'])
        # print(request.session['passageid'])
    except Exception:
        request.session['status'] = 0
    # request.session['status'] = 0
    # print(request.session['username'])
    # res = AnswerSearcher()
    # ans = res.getRelationByName('丹益片')
    # for i in ans:
    #     print(i['rel'])
    # print(ans[0])
    # print(ans)

    return render(request, 'index.html', {'session': request.session})


def single(request):
    # 测试用，大部分功能页面的模板
    return render(request, 'single.html')


def login(request):
    if request.method == "POST":
        user = Users.objects.filter(email=request.POST['email'], password=request.POST['password'])
        if len(user) == 0:
            messages.error(request, '邮箱或密码错误!')
            return render(request, 'login.html')
        request.session['user_id'] = user[0].id
        request.session['username'] = user[0].username
        request.session['group'] = user[0].group
        request.session['status'] = 1
        # print(user[0].username)
        # messages.success(request, '登录成功!')
        return render(request, 'index.html', {'session': request.session})
    else:
        return render(request, 'login.html', {'session': request.session})


def logout(request):
    request.session['status'] = 0
    return render(request, 'index.html', {'session': request.session})


def passageindex(request):
    passages = Article.objects.all()
    # a = Article(paragraph_1='1234567\n3813801238091283091283', title='test',
    #             paragraph_2='dhlawhlihiulafiuf\naidhodhiahd\ndjaijda', image='/', author='123')
    # a.save()
    return render(request, 'passageindex.html', {'session': request.session, 'passages': passages})


def getpassage(request):
    # print(request.POST.get('passageid'))
    passage = Article.objects.filter(id=request.POST.get('passageid'))
    return render(request, 'passage.html', {'session': request.session, 'passage': passage})


def searchresult(request):
    if request.method == 'POST':
        a1 = str(request.POST['a1'])
        # ans是关系数据库查询
        ans = []
        ansname = []
        if a1 != '':
            data = BasicData.objects.all()
            for i in data:
                if a1 in i.name and not i.name in ansname:
                    ansname += [i.name]
                    ans += [i]

        # neoans是图数据库查询
        res = AnswerSearcher()
        neoans = res.getRelationByName(a1)
        neonum = len(neoans)

        # for i in ans:
        #     print(i.id,' ',i.name)
        return render(request, 'searchresult.html',
                      {'session': request.session, 'ans': ans, 'a1': a1, 'size': len(ans),
                       'graph': json.dumps(neoans, ensure_ascii=False), 'neonum': neonum})
    else:
        return render(request, 'searchresult.html', {'session': request.session})


def qs(request):
    qshistory = QSHistory.objects.all().order_by('-id')

    return render(request, 'qs.html', {'session': request.session, 'qshistory': qshistory})


def submitsatisfaction(request):
    if request.method == 'POST':
        id1 = request.POST.get('id')
        satis = request.POST.get('satis')
        QSHistory.objects.filter(id=id1).update(satisfy=satis)
    qshistory = QSHistory.objects.all().order_by('-id')
    return render(request, 'qs.html', {'session': request.session, 'qshistory': qshistory})


def question(request):
    if request.method == 'POST':
        user_qs = request.POST['a1']
        handler = ChatBotGraph()
        ans = handler.chat_main(user_qs)
        qsht = QSHistory(question=user_qs, ans=ans, satisfy=-1, user=request.session['username'])
        qsht.save()
    qshistory = QSHistory.objects.all().order_by('-id')

    return render(request, 'qs.html', {'session': request.session, 'qshistory': qshistory})


def sendemail(request):
    if request.method == 'POST':
        # sendemail()
        messages.success(request, '发送成功！')
    return render(request, 'index.html', {'session': request.session})


def subscribe(request):
    if request.method == 'POST':
        # subscribe()
        messages.success(request, '订阅成功！')
    return render(request, 'index.html', {'session': request.session})


def register(request):
    if request.method == 'POST':
        hasReg = Users.objects.filter(email=request.POST['email'])
        if len(hasReg) > 0:
            messages.error(request, '当前邮箱已有人注册！请检查是否已注册或换个邮箱再试试')
        else:
            user = Users(email=request.POST['email'], password=request.POST['password'], username=request.POST['name'],
                         group=0)
            user.save()
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['group'] = user.group
            request.session['status'] = 1
            messages.success(request, '注册成功！已为您自动登录')
            return render(request, 'index.html', {'session': request.session})

    return render(request, 'register.html', {'session': request.session})


def recommend(request):
    id1 = random.choice(range(1, 1000))
    a = BasicData.objects.filter(id=id1)
    return render(request, 'recommend.html', {'session': request.session, 'a0': a})
