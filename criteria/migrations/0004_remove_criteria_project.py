# Generated by Django 4.0.4 on 2022-04-19 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0003_criteria_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='project',
        ),
    ]