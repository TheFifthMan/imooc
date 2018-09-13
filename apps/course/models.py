from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name="课程名称")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=(('low','初级'),('medium','中级'),('high','高级')),max_length=6,verbose_name='课程难度')
    learn_time = models.IntegerField(verbose_name="学习时长")
    students = models.IntegerField(verbose_name="学习人数")
    fav_nums = models.IntegerField(verbose_name="收藏人数")
    images = models.ImageField(upload_to='imgage/courses/%Y/%m/%d',default="images/courses/default.jpg",verbose_name="课程图片")
    click_nums = models.IntegerField(verbose_name="点击次数")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    
    def __str__(self):
        return self.name



    class Meta:
        db_table = 'course'
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    name = models.CharField(max_length=100,verbose_name="课程章节名称")
    course = models.ForeignKey('Course',on_delete=models.CASCADE,related_name='lessons',verbose_name="对应的课程")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    
    
    def __str__(self):
        return self.name


    class Meta:
            db_table = 'lesson'
            verbose_name = "课程章节信息"
            verbose_name_plural = verbose_name

class Video(models.Model):
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE,related_name='videoes',verbose_name = '对应的章节')
    name = models.CharField(max_length=100,verbose_name="视频名字")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    
    
    def __str__(self):
        return self.name


    class Meta:
            db_table = 'video'
            verbose_name = "课程章节视频信息"
            verbose_name_plural = verbose_name

class CourseResource(models.Model):
    name = models.CharField(max_length=100,verbose_name="资源名称")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    course = models.ForeignKey('Course',on_delete=models.CASCADE,related_name='resources',verbose_name='课程')
    download = models.FileField(max_length=100,verbose_name='下载地址')


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'course_resource'
        verbose_name = "课程资源信息"
        verbose_name_plural = verbose_name
