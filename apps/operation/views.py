from django.shortcuts import render,HttpResponse
from .forms import UserAskForm
from .models import UserAsk
from django.views import View
import json


# Create your views here.
class UserAskView(View):
    def post(self,request):
        form = UserAskForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
           res = {'status':'success'}
           return HttpResponse(json.dumps(res),content_type='application/json')
        else:
            res = {'status':'fail'}
            return HttpResponse(json.dumps(res),content_type='application/json')



