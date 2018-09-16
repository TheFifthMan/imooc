from django.shortcuts import render
from django.views import View
from .models import CityDict,CourseOrganization,OrgType

# Create your views here.
class OrgListView(View):
    def get(self,request):
        city_list = CityDict.objects.all()
        org_type_list = OrgType.objects.all()
        org_list = CourseOrganization.objects.all()
        return render(request,'org-list.html',{'city_list':city_list,'org_type_list':org_type_list,'org_list':org_list})