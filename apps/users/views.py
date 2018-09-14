from django.shortcuts import render,redirect,HttpResponse
from .models import UserProfile,EmailVerifyRecord
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,ForgetPasswordForm,SendEmailForResetPasswdForm
from django.urls import reverse
from utils.email import send_email


# Create your views here.
# 用于重置认证机制
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

# 首页
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

# 用于注册用户
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
            send_email(email,'register')
            return redirect(reverse('login'))
        else:
            return render(request,"register.html",{'form':form})

# 填入邮件地址，用于发送邮件
class SendEmailForResetPasswdView(View):
    def get(self):
        form = SendEmailForResetPasswdForm()
        return render(request,'send_email_for_reset_passwd.html',{'form':form})

    def  post(self):
        form = SendEmailForResetPasswdForm(data=request.POST)
        email = request.POST.get('email','')
        if form.is_valid():
            send_email(email,type_name="forget")
        
        return HttpResponse("已经发送成功，请注意查收邮件")

# 用于重置密码
class ForgetPasswordView(View):
    def get(self,request,code):
        try:
            record = EmailVerifyRecord.objects.get(code=code)
            if record.send_type == 'forget' and record.is_used = False:
                form = ForgetPasswordForm()
                return render(request,'forget_password.html',{"form":form})
        except Exception as e:
            pass

        return HttpResponse("The link is expired")
    
    def post(self,request,code):
        form = ForgetPasswordForm(data=request.POST)
        record = EmailVerifyRecord.objects.get(code=code)
        if form.is_valid() and record.is_used = False:
            user = UserProfile.objects.get(email=record.email)
            new_password = request.POST.get('new_password','')
            user.set_password(new_password)
            user.save()
            record.is_used = True
            record.save()
            return redirect(reverse('login'))
        
        return redirect(reverse('forget_password'))

# 用于激活用户
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

# 用于注销用户
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('index'))

# 用于登录用户
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