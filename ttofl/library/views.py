from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib import messages


# Create your views here.
def index(request):
    # if request.session['user'] !=None:
    #     return render(request,'index.html')
    # else:
    #     return redirect(login_page)
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def login_page(request):
    return render(request,'login.html')

def admin_login(request):
    return render(request,'admin.html')

def book_details(request):
    if request.method=='POST':
        books=books_data1(
            name=request.POST['name'],
            author_name=request.POST['author_name'],
            genre=request.POST['genre'],
            pages=request.POST['pages'],
            email=request.session['user']
        )
        books.save()
        print("book data is recorded")
        return render(request,'books_data.html')
@api_view(['GET','POST'])
def admin(request):
    if request.method=='POST':
        admin_id="ttofl@gmail.com"
        admin_password="ttofl"
        if request.POST['email1']==admin_id and request.POST['password']==admin_password:
            print("credentials are valid")
            data=books_data1.objects.all()
            author_details={
                'data':data
            }
            return render(request,'admin_page.html',context=author_details)
        else:
            print("credientials are invalid")

        return render(request,'admin.html')
    
    if request.method=='GET':
        return render(request,'admin_page.html')
def login(request):
    if request.method=='POST':
        email_test=request.POST['email1']
        password=request.POST['password']

        if books_1.objects.filter(email=email_test).exists() and books_1.objects.filter(email=email_test).values('password').first()['password']==password:
            request.session['user']=email_test
            print("successful login")
            return render(request,'books_data.html')
        else:
            print("Invalid credientials")
            return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    if request.session['user']:
        request.session['user']=None
        print(request.session['user'])
        print("successful logout")
        return render(request,'login.html')

@api_view(['GET','POST'])
def home_page(request):
    if request.method=='POST':
        city1=request.POST['city']
        cty=city1.upper()
        a=cty[:3]
        count=books_1.objects.filter(city=city1).count()
        if count!=0:
            count+=1
        else:
            count=1
        unique_code="AR"+a+str(count)
        print(unique_code)
            
        if books_1.objects.filter(email=request.POST['email']).exists():
            print("Already account created")
            return render(request,'index.html')
        else:
            print("created")
            user=books_1(
                    # user_id=request.session['user'],
                    user_id=unique_code,
                    name=request.POST['name'],
                    phone=request.POST['contact_details'],
                    email=request.POST['email'],
                    city=city1,
                    profile_image=request.FILES['profile_image'],
                    password=request.POST['password']
                )
            user.save()
        return render(request,'index.html')
    if request.method=='GET':
        print(request.session['user'])
        obj=books_data1.objects.filter(email=request.session['user']).all()
        data1={
            'serializer':obj
        }
        return render(request,'images.html',context=data1)
