from collections import UserDict
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
import csv,smtplib,os,ssl,random
x='bruh -_-'


def signup(request):
    if request.method == 'POST':
        UsName=request.POST['UserName']
        Email=request.POST['Email']
        Fname=request.POST['FirstName']
        Lname=request.POST['LastName']
        PsWord=request.POST['Pass1']
        CPsWord=request.POST['Pass2']
        #myuser=User.objects.create()
        if PsWord==CPsWord:
            f=open('db.csv','w')
            w=csv.writer(f)
            #([UsName,Email,Fname,Lname,PsWord])
            w.writerow([UsName,Email,Fname,Lname,PsWord])
            f.close()
            return render(request, 'sign in.html')
        else:
            messages.error(request, "Failed")
            return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        UsName=request.POST['UserName']
        PsWord=request.POST['PassWord']
        Otp=request.POST['OTP']
        #Otp=request.POST['OTP']
        f=open('db.csv','r')
        data=csv.reader(f)
        
        for i in data:
            if i[0]==UsName:
                if i[4]==PsWord:
                    info=i
                    return render(request,'CsProject.html',{'info':info})
    return render(request,'login.html')


def home(request):
    return render(request,'CsProject.html',{'summa':x})

def Admin(request):
    if request.method == 'POST':
        UsName=request.POST['UserName']
        PsWord=request.POST['PassWord']
        f=open('Adb.csv','r')
        data=csv.reader(f)
        
        for i in data:
            if i[0]==UsName:
                if i[4]==PsWord:
                    info=i
                    return render(request,'CsProject.html',{'info':info})
    return render(request,'admin.html')

def pg2_1(request):
    return render(request,'2ndpage1_1.html')

def pg2_2(request):
    return render(request,'2ndpage2.html')

def pg2_3(request):
    return render(request,'2ndpage3.html')

def pg2_4(request):
    return render(request,'2ndpage4.html')

def pg3(request):
    return render(request,'3rdpage.html')

def payment(request):
    if request.method == 'POST':
        FulName=request.POST['FulName']
        Email=request.POST['Email']
        Address=request.POST['Address']
        City=request.POST['City']
        State=request.POST['State']
        Zip=request.POST['Zip']
        Card=request.POST['Card']
        CardNo=request.POST['CardNo']
        ExptMonth=request.POST['ExptMonth']
        ExptYear=request.POST['ExptYear']
        Cvv=request.POST['Cvv']
        a=([FulName,Email,Address,City,State,Zip,Card,CardNo,ExptMonth,ExptYear,Cvv])
    return render(request,'payment.html')

def mail(ead,sub,bod):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('nitinstrange2439@gmail.com', 'lonqzqzvfahzrfkj')
        msg = f'Subject: {sub}\n\n{bod}'
        smtp.sendmail('nitin@svstudent.in',ead,msg)

def OTP(n):
    for i in range(n):
        return(random.randrange(1,10))

def OTPRequest(request):
    email=request.POST.get('Email')
    a=OTP(6)
    b='Your OTP is:'
    c=str(a)+b
    mail(email,"Your OTP",c)
    if 0==0:
        return render(request,'login.html',{'OTP':a})
    return render(request,'OTPRequest.html')