from django.test import TestCase

# Create your tests here.
from organization.models import CityDict,CourseOrganization,OrgType
from mimesis.enums import Gender
from mimesis import Address,Development
import random

if __name__ =="__main__":
    zh = Address('zh')
    c = Development()
    citys = ["上海","北京","杭州","深圳","广东"]
    
    for i in citys:
        city = CityDict(name=i,desc="test")
        city.save()
        for i in range(100):
            org = CourseOrganization(name=c.backend(),
                                    desc = c.programming_language(),
                                    click_num=i*random.randint(1,1000),
                                    fav_nums = i*random.randint(1,1000),
                                    address = zh.address())
            org.city = city
            org.save()

'''
delete from city_dict;
delete from course_organization;
select * from city_dict;
select * from course_organization;
'''