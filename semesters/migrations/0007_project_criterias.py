# Generated by Django 4.0.4 on 2022-04-19 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0002_remove_criteria_project'),
        ('semesters', '0006_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='criterias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='criteria.criteria'),
        ),
    ]
