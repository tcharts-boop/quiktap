# Generated by Django 3.0.10 on 2020-09-23 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200922_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_content',
        ),
    ]
