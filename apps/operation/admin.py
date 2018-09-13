from django.contrib import admin
from operation.models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse
# Register your models here.

class UserAskAdmin(admin.ModelAdmin):
    list_display = ['name',"mobile","course_name","add_time"]
    list_per_page = 20
    search_fields = ['name',"mobile","course_name"]
    list_filter = ['name',"mobile","course_name","add_time"]

class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = ["course","user","comment","add_time"]
    list_per_page = 20
    search_fields = ["course","user","comment"]
    list_filter = ["course","user","comment","add_time"]


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ["user","fav_id","fav_type","add_time"]
    list_per_page = 20
    search_fields = ["user","fav_id","fav_type"]
    list_filter = ["user","fav_id","fav_type","add_time"]


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ["user","message","add_time","has_read"]
    list_per_page = 20
    search_fields = ["user","message","has_read"]
    list_filter =  ["user","message","add_time","has_read"]

class UserCourseAdmin(admin.ModelAdmin):
    list_display = ["user","course","add_time"]
    list_per_page = 20
    search_fields = ["user","course"]
    list_filter =  ["user","course","add_time"]


admin.site.register(UserAsk,UserAskAdmin)
admin.site.register(CourseComments,CourseCommentsAdmin)
admin.site.register(UserFavorite,UserFavoriteAdmin)
admin.site.register(UserMessage,UserMessageAdmin)
admin.site.register(UserCourse,UserCourseAdmin)

