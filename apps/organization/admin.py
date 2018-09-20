from django.contrib import admin
from organization.models import CourseOrganization,CityDict,Teacher,OrgType
# Register your models here.
class CourseOrganizationAdmin(admin.ModelAdmin):
    list_display = ['name','desc','fav_nums','image','click_num','add_time',"address","city"]
    list_per_page = 20
    search_fields = ['name','desc','fav_nums','image','click_num',"address","city"]
    list_filter = ['name','desc','fav_nums','image','click_num','add_time',"address","city"]
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ['name','add_time',"org",]
    list_per_page = 20
    search_fields = ['name','org']
    list_filter = ['name','org']
class CityDictAdmin(admin.ModelAdmin):
    list_display = ["name","desc","add_time"]
    list_per_page = 20
    search_fields = ["name","desc"]
    list_filter = ["name","desc","add_time"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name","work_years","company","desc","click_nums","fav_nums","position","org","add_time"]
    list_per_page = 20
    search_fileds =  ["name","work_years","company","desc","click_nums","fav_nums","position","org"]
    list_filter =["name","work_years","company","desc","click_nums","fav_nums","position","org","add_time"]


admin.site.register(CourseOrganization,CourseOrganizationAdmin)
admin.site.register(CityDict,CityDictAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(OrgType,OrgTypeAdmin)
