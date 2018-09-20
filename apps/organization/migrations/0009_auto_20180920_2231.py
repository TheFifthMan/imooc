# Generated by Django 2.1.1 on 2018-09-20 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_auto_20180920_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydict',
            name='orgtype',
            field=models.ManyToManyField(related_name='city', to='organization.OrgType'),
        ),
        migrations.AlterField(
            model_name='orgtype',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='机构类别'),
        ),
    ]