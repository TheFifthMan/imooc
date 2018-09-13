from django.db import models
from course.models import Course
from users.models import UserProfile

# Create your models here.
class UserAsk(models.Model):
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机号码',max_length=11)
    course_name = models.CharField('课程名称',max_length=50)
    add_time = models.DateTimeField('添加时间',auto_now_add=True)

    class Meta:
        db_table = 'user_ask'
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField('评论',max_length=400)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_comments'
        verbose_name = "课程留言"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='favorites')
    fav_id = models.IntegerField('喜欢类型id')
    fav_type = models.IntegerField('喜欢的类型',choices=((1,'课程'),(2,'机构组织'),(3,'讲师')))
    add_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'user_favorite'
        verbose_name = "用户喜欢的信息"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField('用户ID',default=0)
    message = models.CharField('用户消息',max_length=500)
    add_time = models.DateTimeField('添加时间',auto_created=True)
    has_read = models.BooleanField(default=False)


    class Meta:
        db_table = 'user_message'
        verbose_name = "用户接受的消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=True)
    add_time = models.DateTimeField('添加时间',auto_created=True)


    class Meta:
        db_table = 'user_course'
        verbose_name = "用户和课程的对应关系"
        verbose_name_plural = verbose_name

