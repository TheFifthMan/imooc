# Generated by Django 2.1.1 on 2018-09-10 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('low', '初级'), ('medium', '中级'), ('high', '高级')], max_length=6, verbose_name='课程难度')),
                ('learn_time', models.IntegerField(verbose_name='学习时长')),
                ('students', models.IntegerField(verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(verbose_name='收藏人数')),
                ('images', models.ImageField(default='images/courses/default.jpg', upload_to='imgage/courses/%Y/%m/%d', verbose_name='课程图片')),
                ('click_nums', models.IntegerField(verbose_name='点击次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='资源名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('download', models.FileField(upload_to='', verbose_name='下载地址')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='course.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源信息',
                'verbose_name_plural': '课程资源信息',
                'db_table': 'course_resource',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='课程章节名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.Course', verbose_name='对应的课程')),
            ],
            options={
                'verbose_name': '课程章节信息',
                'verbose_name_plural': '课程章节信息',
                'db_table': 'lesson',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名字')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videoes', to='course.Lesson', verbose_name='对应的章节')),
            ],
            options={
                'verbose_name': '课程章节视频信息',
                'verbose_name_plural': '课程章节视频信息',
                'db_table': 'video',
            },
        ),
    ]
