from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20)
    birthday = models.DateField(verbose_name="生日",null=True,blank=True)
    gender = models.CharField(choices=(('man','男'),('female','女')),max_length=6,verbose_name="性别")
    address = models.CharField(max_length=100,verbose_name="地址")
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name="电话")
    image = models.ImageField(upload_to="images/users/user/%Y/%m/%d",default='images/users/default.jpg',verbose_name="头像",max_length=100)


    def __str__(self):
        return self.nick_name


    class Meta:
        db_table = 'user_profile'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(verbose_name="邮箱地址")
    send_type = models.CharField(choices=(("register","注册"),("forget","忘记密码")),max_length=10,verbose_name="发送类型")
    send_time = models.DateTimeField(auto_now_add=True,verbose_name="发送时间")
    is_used = models.BooleanField(default=False)

    
    def __str__(self):
        return self.code


    class Meta:
        db_table = 'email_verify_record'
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="图片标题")
    image = models.ImageField(upload_to="images/users/banner/%Y/%m/%d",max_length=100,verbose_name="图片地址")
    url = models.URLField(verbose_name="课程跳转的地址")
    index = models.IntegerField(verbose_name="图片序列",default=100)
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")


    def __str__(self):
        return self.title


    class Meta:
        db_table = 'banner'
        verbose_name = "首页轮播图"
        verbose_name_plural = verbose_name