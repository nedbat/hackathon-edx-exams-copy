# Generated by Django 3.2.15 on 2022-09-28 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_exam_exam_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='anonymous_user_id',
        ),
    ]
