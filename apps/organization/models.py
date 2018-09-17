from django.db import models
from course.models import Course
# Create your models here.
class OrgType(models.Model):
    name = models.CharField(max_length=20,verbose_name="机构类别")
    add_time = models.DateTimeField(auto_created=True)
    org = models.ForeignKey('CourseOrganization',on_delete=models.CASCADE,related_name='org_type')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'org_type'
        verbose_name = '机构类别'
        verbose_name_plural = verbose_name

class CourseOrganization(models.Model):
    name = models.CharField(max_length=50,verbose_name='课程组织名字')
    desc = models.TextField(verbose_name="组织描述")
    click_num = models.IntegerField(default=0,verbose_name="点击次数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏次数")
    image = models.ImageField(upload_to='images/org/%Y/%m/%d',default='images/org/default.jpg')
    address = models.CharField(max_length=150,verbose_name="地址")
    city = models.ForeignKey('CityDict',on_delete=models.CASCADE,related_name='organizations',verbose_name="所属城市")
    add_time = models.DateTimeField('添加时间',auto_now_add=True)
    courses = models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE,related_name='org')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_organization'
        verbose_name = "课程组织信息"
        verbose_name_plural = verbose_name

class CityDict(models.Model):
    name = models.CharField('城市名称',max_length=150)
    add_time = models.DateTimeField('添加时间',auto_now_add=True)
    desc = models.CharField('描述',max_length=200)


    def __str__(self):
        return self.name

    class Meta:
            db_table = 'city_dict'
            verbose_name = "城市"
            verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField('老师名字',max_length=100)
    work_years = models.IntegerField('工作年限')
    company = models.CharField('公司',max_length=100)
    position = models.CharField('职位',max_length=120)
    desc = models.CharField('教学特点',max_length=300)
    click_nums = models.IntegerField('点击次数')
    fav_nums = models.IntegerField('喜欢人数')
    add_time = models.DateTimeField('添加时间',auto_now_add=True)
    org = models.ForeignKey('CourseOrganization',on_delete=models.CASCADE,related_name='teachers',verbose_name='所属组织')


    def __str__(self):
        return self.name

        
    class Meta:
        db_table = 'teacher'
        verbose_name = "老师信息"
        verbose_name_plural = verbose_name
