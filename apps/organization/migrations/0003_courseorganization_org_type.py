# Generated by Django 2.1.1 on 2018-09-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180913_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='org_type',
            field=models.CharField(default='培训机构', max_length=20, verbose_name='组织机构类别'),
        ),
    ]
