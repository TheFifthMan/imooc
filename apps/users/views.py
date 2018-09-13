from django.shortcuts import render,redirect,HttpResponse
from .models import UserProfile,EmailVerifyRecord
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.urls import reverse
from utils.email import send_register_email


# Create your views here.
class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

# 暂时无错误提示信息
class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get('email','')
            username=request.POST.get('username','')  
            password=request.POST.get('password','')  
            user = UserProfile(username=username,email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            send_register_email(email)
            return redirect(reverse('login'))
        else:
            return render(request,"register.html",{'form':form})

class ActivateView(View):
    def get(self,request,activate_code):
        try:
            record = EmailVerifyRecord.objects.get(code=activate_code)
            if not record.is_used:
                u = UserProfile.objects.get(email=record.email)
                u.is_active = True
                record.is_used = True
                record.save()
                u.save()
                return redirect(reverse('login'))
        except Exception as e:
            print(e)
        
        return HttpResponse('验证连接不存在！')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('index'))

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{"form":form})
    
    def post(self,request):
        # 把表单数据传入验证
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return redirect(reverse("index"))
           
        return render(request,'login.html',{'form':form})