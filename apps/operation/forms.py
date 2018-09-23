from django.forms import ModelForm,ValidationError
from .models import UserAsk

class UserAskForm(ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','course_name','mobile']


        