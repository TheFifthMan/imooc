from django.urls import path,include,re_path
from operation.views import UserAskView

urlpatterns = [
    path('add_ask/',UserAskView.as_view(),name='operation')
]