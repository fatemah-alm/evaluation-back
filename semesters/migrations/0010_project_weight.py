# Generated by Django 4.0.4 on 2022-04-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semesters', '0009_project_criterias'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
