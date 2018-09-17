"""imooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from users.views import LoginView,IndexView,RegisterView,LogoutView,ActivateView,PasswordReset,ForgetPasswordView
from organization.views import OrgDetailTeachersView,OrgDetailHomePageView,TeachersListView,OrgDetailDescView,OrgListView,OrgDetailCourseView
from imooc.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/', include('captcha.urls')),
    re_path(r'^register/(?P<activate_code>\w+)$',ActivateView.as_view(),name='activate'),
    re_path(r'^forget/(?P<code>\w+)$',PasswordReset.as_view(),name='password_reset'),
    path('forgetpwd',ForgetPasswordView.as_view(),name='forgetpwd'),
    path('orglist/',OrgListView.as_view(),name='orglist'),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    path('org-detail-course/',OrgDetailCourseView.as_view(),name='org_detail_course'),
    path('org-detail-desc/',OrgDetailDescView.as_view(),name='org_detail_desc'),
    path('org-detail-homepage/',OrgDetailHomePageView.as_view(),name='org_detail_homepage'),
    path('org-detail-teachers/',OrgDetailTeachersView.as_view(),name='org_detail_teachers'),
    path('teachers-list/',TeachersListView.as_view(),name='teachers-list'),
]
