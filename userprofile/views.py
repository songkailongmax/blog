from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from .forms import ProfileForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.clean()
            user = authenticate(username=data['user_name'], password=data['user_pwd'])
            if user:
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse('账号或密码错误，请重新输入！')
        else:
            return HttpResponse('账号或密码不合法，请重新输入！')
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'user_login_form': user_login_form}
        return render(request=request, template_name='userprofile/login.html', context=context)
    else:
        return HttpResponse('请使用post或get请求!')


def user_logout(request):
    logout(request)
    return redirect('article:article_list')


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('article:article_list')
        else:
            return HttpResponse('注册表单输入有误，请重试输入！')
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'user_register_form': user_register_form}
        return render(request=request, template_name='userprofile/register.html', context=context)
    else:
        return HttpResponse('请使用post或get请求!')


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('article:article_list')
        else:
            return HttpResponse('您没有删除权限')
    else:
        return HttpResponse('not support post request!')


@login_required(login_url='/userprofile/login')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)
    if request.method == 'POST':
        if request.user != user:
            return HttpResponse('您没有操作权限～')
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd['avatar']
            profile.save()
            return redirect('userprofile:edit', id)
        else:
            return HttpResponse('表单提交有误，请重新输入')
    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse('仅支持post和get请求')
