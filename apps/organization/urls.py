from organization.views import OrgDetailTeachersView,OrgDetailHomePageView,TeachersListView,OrgDetailDescView,OrgListView,OrgDetailCourseView
from django.urls import path,include,re_path

urlpatterns = [
    path('org-detail-course/',OrgDetailCourseView.as_view(),name='org_detail_course'),
    path('org-detail-desc/',OrgDetailDescView.as_view(),name='org_detail_desc'),
    path('org-detail-homepage/',OrgDetailHomePageView.as_view(),name='org_detail_homepage'),
    path('org-detail-teachers/',OrgDetailTeachersView.as_view(),name='org_detail_teachers'),
    path('teachers-list/',TeachersListView.as_view(),name='teachers-list'),
    path('orglist/',OrgListView.as_view(),name='orglist'),
]
