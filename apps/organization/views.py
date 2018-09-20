from django.shortcuts import render
from django.views import View
from .models import CityDict,CourseOrganization,OrgType
from course.models import Course
from users.models import UserProfile
from django.core.paginator import Paginator
from imooc.settings import LIMIT

# Create your views here.
class OrgListView(View):
    def get(self,request):
        city_list = CityDict.objects.all()
        org_type_list = OrgType.objects.all()
        org_list = CourseOrganization.objects.all()
        city = request.GET.get('city')
        ty = request.GET.get('ty')
        cityobj = ''
        org_type = ''

        if city:
            cityobj = CityDict.objects.get(pk=city)
            
        if ty:
             org_type = OrgType.objects.get(pk=ty)

        if city and ty:
            org_list = CourseOrganization.objects.filter(city=city,orgtype=ty)

        hot_orgs = CourseOrganization.objects.all().order_by('-click_num')[:3]

        sort = request.GET.get('sort')
        if sort == 'students':
            org_list = org_list.order_by('-students')
        
        elif sort == 'courses':
            org_list = org_list.order_by('-courses')
            
        # 分页
        paginator = Paginator(org_list,LIMIT)
        page = request.GET.get('page','1')
        result = paginator.page(page)
        org_count = org_list.count()
        course_count = Course.objects.all().count()
        user_count = UserProfile.objects.all().count()
        return render(request,'org-list.html',
                            {'city_list':city_list,
                            'cityobj':cityobj,
                            'ty':org_type,
                            'org_type_list':org_type_list,
                            'org_list':result.object_list,
                            'course_count':course_count,
                            'user_count':user_count,
                            'org_count':org_count,
                            'hot_orgs':hot_orgs,
                            })


class OrgDetailCourseView(View):
    def get(self,request):
        return render(request,'org-detail-course.html')



class OrgDetailDescView(View):
     def get(self,request):
            return render(request,'org-detail-desc.html')




class OrgDetailHomePageView(View):
     def get(self,request):
            return render(request,'org-detail-homepage.html')




class OrgDetailTeachersView(View):
     def get(self,request):
            return render(request,'org-detail-teachers.html')



class TeachersListView(View):
     def get(self,request):
            return render(request,'teachers-list.html')
