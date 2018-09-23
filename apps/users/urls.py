from django.urls import path,include,re_path
from users.views import LoginView,IndexView,RegisterView,LogoutView,ActivateView,PasswordReset,ForgetPasswordView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    re_path(r'^register/(?P<activate_code>\w+)$',ActivateView.as_view(),name='activate'),
    re_path(r'^forget/(?P<code>\w+)$',PasswordReset.as_view(),name='password_reset'),
    path('forgetpwd',ForgetPasswordView.as_view(),name='forgetpwd'),
]