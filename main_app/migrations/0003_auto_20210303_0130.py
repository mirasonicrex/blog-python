# Generated by Django 3.1.7 on 2021-03-03 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_delete', 'Can delete post')]},
        ),
    ]
