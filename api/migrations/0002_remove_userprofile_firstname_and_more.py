# Generated by Django 4.1.7 on 2023-05-26 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastName',
        ),
    ]
