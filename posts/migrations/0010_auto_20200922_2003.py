# Generated by Django 3.0.10 on 2020-09-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200922_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_content',
            field=models.ImageField(blank=True, default='', upload_to='post_images'),
        ),
    ]
