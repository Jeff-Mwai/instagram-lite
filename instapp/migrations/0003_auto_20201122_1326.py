# Generated by Django 3.1.3 on 2020-11-22 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0002_auto_20201121_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='user',
        ),
    ]
