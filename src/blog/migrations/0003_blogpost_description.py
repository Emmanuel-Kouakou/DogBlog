# Generated by Django 3.1.6 on 2023-06-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230621_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]