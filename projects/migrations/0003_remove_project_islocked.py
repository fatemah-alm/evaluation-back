# Generated by Django 4.0.4 on 2022-04-25 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_islocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='isLocked',
        ),
    ]
