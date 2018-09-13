
from django import forms
from django.forms import ValidationError
from .models import UserProfile
from captcha.fields import CaptchaField


# https://www.jianshu.com/p/7e61160dc689
# https://blog.csdn.net/u013703139/article/details/72770614

class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={"name":"username","id":"account_l","type":"text","placeholder":"手机号/邮箱"}),
                               error_messages={
                                    "required":"用户名不能为空",
                                    "max_length":"不能超过20个字符"
                                })

    password = forms.CharField(required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "name":"password",
                                        "id":"password_l",
                                        "type":"password",
                                        "placeholder":"请输入您的密码" 
                                        }),
                                error_messages={
                                    "required":"用户名不能为空",
                                    "max_length":"不能超过20个字符"
                                })
    login_captcha = CaptchaField()


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,
                            widget = forms.TextInput(
                                attrs={
                                    "type":"text",
                                    "id":"id_email",
                                    "name":"email",
                                    "placeholder":"请输入您的邮箱地址",
                                }
                            ),
                            error_messages={
                                "required":"email不能为空",                               
                            })
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={"name":"username","id":"account_l","type":"text","placeholder":"昵称"}),
                               max_length=20,
                               error_messages={
                                    "required":"用户名不能为空",
                                    "max_length":"不能超过20个字符"
                                })
    
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    "type":"password",
                                    "id":"id_password",
                                    "name":"password",
                                    "placeholder":"请输入6-20位非中文字符密码"
                                }),
                                min_length=8,
                                error_messages={
                                    "required":"密码不能为空",
                                    "min_length":"不能少于8个字符",
                                }
                            )
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    "type":"password",
                                    "id":"id_password2",
                                    "name":"password2",
                                    "placeholder":"请输入6-20位非中文字符密码"
                                }),
                                 min_length=8,
                                error_messages={
                                    "required":"密码不能为空",
                                    "min_length":"不能少于8个字符"
                                }
                            )
    captcha = CaptchaField()

    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data['username']
        email = cleaned_data['email']
        pwd = cleaned_data['password']
        pwd2 = cleaned_data['password2']
        if pwd != pwd2:
            raise ValidationError('两次密码不一致')
        
        email = UserProfile.objects.filter(email=email)
        if email :
            raise ValidationError("邮箱已经存在！")

        username = UserProfile.objects.filter(username=username)
        if username:
            raise ValidationError("昵称已经被占用")
        
        return cleaned_data

