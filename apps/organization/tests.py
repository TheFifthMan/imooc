from django.test import TestCase

# Create your tests here.
from organization.models import CityDict,CourseOrganization,OrgType
from mimesis.enums import Gender
from mimesis import Address,Development
import random

if __name__ =="__main__":
    zh = Address('zh')
    c = Development()
    for i in range(300):
        citys = ["上海","北京","杭州","深圳","广东"]
        city = CityDict(name=random.choice(citys),desc="test")
        org = CourseOrganization(name=c.backend(),
                                desc = c.programming_language(),
                                click_num=i*random.randint(1,1000),
                                fav_nums = i*random.randint(1,1000),
                                address = zh.address())
        city.save()
        org.city = city
        
        org.save()

    