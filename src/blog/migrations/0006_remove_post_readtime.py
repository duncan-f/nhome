# Generated by Django 2.2 on 2019-06-14 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190514_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='readtime',
        ),
    ]
