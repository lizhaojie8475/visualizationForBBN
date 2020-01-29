from django.shortcuts import render, redirect
from .forms import loginForm
from .models import userModel
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request, url):
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            login_name = login_form.cleaned_data["userName"].strip()
            login_password = login_form.cleaned_data["password"]
            try:
                user = userModel.objects.get(userName=login_name)
                if user.password == login_password:
                    request.session["userName"] = user.userName
                    request.session["authority"] = user.authority
                    messages.add_message(request, messages.SUCCESS, "欢迎您的登录")
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "用户名或密码错误")
            except:
                messages.add_message(request, messages.WARNING, "用户名或密码错误")
        else:
            messages.add_message(request, messages.WARNING, "请检查输入的字段格式是否正确")
    else:
        login_form = loginForm()
    url = url
    return render(request, 'login.html', locals())


def logout(request):
    if 'userName' in request.session:
        Session.objects.all().delete()
        return redirect('/login/')
    return redirect('/')


def index(request, url):
    if 'userName' in request.session:
        userName = request.session["userName"]
        authority = request.session["authority"]
    else:
        return redirect('/login/')
    url = url
    return render(request, 'index.html', locals())

