from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,RegisterForm
import requests     #to get response from other app
from django.contrib.auth.hashers import make_password

def regiser_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            password =make_password(password, salt='random')
            reg_data = {
                "username" : username,
                "email" : email,
                "password" : password
            }
            response = requests.post('http://127.0.0.1:8999/api/users/',data=reg_data)
            if response.status_code==201:
                return HttpResponse("Registration done successfully")
            else:
                return redirect('/register/')

        else:
            return HttpResponse('You are not registered..!')


    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})


def set_session_token(request,token):
    if not request.session.get('user_token'):
        request.session['user_token'] = token


def get_token(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response = requests.post('http://127.0.0.1:8999/gettoken/',
                      data={'username':username,'password':password})
        token_data = response.json()
        resp = "Token is failed to generate"

        if response.status_code == 200:
            if not request.session.get('user_token',None):
                resp = HttpResponse("Token generated successfully")
                set_session_token(request,token_data.get('token',None))
                return HttpResponse(resp)
            else:
                return HttpResponse('User token value is already generated in browser')


        else:
            return HttpResponse(resp)

    else:
        form = LoginForm()
        return render(request,'Login.html',{'form':form})


def get_session_token(request):
    return request.session.get('user_token',None)

def getAllEmps(request):
    user_token = get_session_token(request)

    if not user_token:
        return redirect('/login/')
    else:
        headers = {
            "Authorization" : "Token{}".format(user_token)
        }
        response = requests.get('http://127.0.0.1:8999/api/emps/',headers=headers)

        if response.status_code == 200:
            return HttpResponse(response.text)
        else:
            return HttpResponse(response.text)

def get_emp_by_id(request,pk):
    user_token = request.session.get('user_token',None)
    if not user_token:
        return redirect('/login/')
    headers = {
        "Authorization": "Token{}".format(user_token)
    }
    response = requests.get('http://127.0.0.1:8999/api/emps/'+str(pk)+'/',
                            headers=headers)

    if response.status_code == 200:
        return HttpResponse(response.text)
    else:
        return HttpResponse(response.text)

def del_emp_by_id(request,pk):
    user_token = request.session.get('user_token',None)
    if not user_token:
        return redirect('/login/')
    headers = {
        "Authorization": "Token{}".format(user_token)
    }
    response = requests.delete('http://127.0.0.1:8999/api/emps/'+str(pk)+'/',
                            headers=headers)

    if response.status_code == 204:
        return HttpResponse("Record deleted successfully")
    else:
        return HttpResponse("Resource not available")


def createView(request):
    user_token = request.session.get('user_token',None)
    if not user_token:
        return redirect('/login/')
    headers = {
        "Authorization": "Token{}".format(user_token)
    }
    data = {
        "eno":4,
        "ename":"Rj",
        "esal" : 20000
    }
    response = requests.post('http://127.0.0.1:8999/api/emps/',data=data,headers=headers)

    if response.status_code == 201:
        return HttpResponse(response.text)
    elif response.status_code == 400:
        return HttpResponse(response.text)
    else:
        HttpResponse("Something went wrong")

def UpdateView(request,pk):
    user_token = request.session.get('user_token',None)

    if not user_token:
        return redirect('/login/')
    headers = {
        "Authorization": "Token{}".format(user_token)
    }
    data = {
        "eno":4,
        "ename":"Rj",
        "esal" : 22000
    }
    response = requests.put('http://127.0.0.1:8999/api/emps/'+str(pk)+'/',data=data,headers=headers)

    if response.status_code == 201:
        return HttpResponse(response.text)
    elif response.status_code == 400:
        return HttpResponse(response.text)
    else:
        HttpResponse("Something went wrong")
