from django.contrib import admin
from course.models import Course,Lesson,Video,CourseResource
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','desc','detail','degree','learn_time','students','fav_nums','images','click_nums','add_time']
    list_per_page = 20
    search_fields = ['name','desc','detail','degree','learn_time','students','fav_nums','images','click_nums']
    list_filter = ['name','desc','detail','degree','learn_time','students','fav_nums','images','click_nums','add_time']


class LessonAdmin(admin.ModelAdmin):
    list_display = ["name","course","add_time"]
    list_per_page = 20
    search_fields = ["name","course"]
    list_filter = ["name","course","add_time"]


class VideoAdmin(admin.ModelAdmin):
    list_display = ["name","lesson","add_time"]
    list_per_page = 20
    search_fileds =  ["name","lesson"]
    list_filter = ["name","lesson","add_time"]


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ["name","add_time","course","download"]
    list_per_page = 20
    search_fileds =  ["name","course","download"]
    list_filter = ["name","add_time","course","download"]


admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(CourseResource,CourseResourceAdmin)

