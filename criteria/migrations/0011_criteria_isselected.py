# Generated by Django 4.0.4 on 2022-04-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0010_remove_criteria_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='isSelected',
            field=models.BooleanField(default=False),
        ),
    ]
