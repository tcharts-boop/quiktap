# Generated by Django 3.0.10 on 2020-09-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200922_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_content',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]