# Generated by Django 4.0.4 on 2022-04-21 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0011_criteria_isselected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='isSelected',
        ),
    ]