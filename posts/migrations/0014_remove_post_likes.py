# Generated by Django 3.0.10 on 2020-09-23 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_post_image_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
