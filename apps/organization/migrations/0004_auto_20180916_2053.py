# Generated by Django 2.1.1 on 2018-09-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorganization_org_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorganization',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='点击次数'),
        ),
        migrations.AlterField(
            model_name='courseorganization',
            name='fav_nums',
            field=models.IntegerField(default=0, verbose_name='收藏次数'),
        ),
    ]