from django.contrib import admin
from users.models import UserProfile,EmailVerifyRecord,Banner
# Register your models here.

admin.site.site_header = "imooc后台管理系统" 

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['nick_name','birthday','gender','address','mobile','image']
    list_per_page = 20
    search_fields = ['nick_name','birthday','gender','address','mobile','image']
    list_filter = ['nick_name','birthday','gender','address','mobile','image']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ["code","email","send_type",'send_time']
    list_per_page = 20
    search_fields = ["code","email","send_type"]
    list_filter = ["code","email","send_type",'send_time']

class BannerAdmin(admin.ModelAdmin):
    list_display = ["title","image","url",'index','add_time']
    list_per_page = 20
    search_fileds =  ["title","image","url",'index']
    list_filter = ["title","image","url",'index','add_time']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(Banner,BannerAdmin)

