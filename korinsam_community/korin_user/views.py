from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Kuser
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    user_id = request.session.get('user')

    if user_id:
        kuser = Kuser.objects.get(pk=user_id)
        return HttpResponse(kuser.user_name)
    return HttpResponse('HOME!!!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def korin_user_login(request):
    if request.method == 'GET':
        return render(request, 'korin_user_login.html')
    elif request.method == 'POST':
        userId = request.POST.get('userId', None)
        password = request.POST.get('password', None)
        
        res_data = {}
        if not(userId and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            kuser = Kuser.objects.get(user_id=userId)
            if check_password(password, kuser.user_pw):
                request.session['user'] = kuser.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'
        return render(request, 'korin_user_login.html', res_data)
    

def korin_user_reg(request):

    if request.method == 'GET':
        return render(request, 'korin_user_reg.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        userId = request.POST.get('userId', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data ={}

        if not (username and userId and password and re_password):
            res_data['error'] = '모든 값을 입력 해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            kuser = Kuser(
                user_name = username,
                user_id = userId,
                user_pw = make_password(password),
            )
            kuser.save()
        return render(request, 'korin_user_reg.html', res_data)
