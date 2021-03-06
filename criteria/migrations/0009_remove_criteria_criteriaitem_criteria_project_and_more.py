# Generated by Django 4.0.4 on 2022-04-20 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semesters', '0015_remove_project_criterias'),
        ('criteria', '0008_criteria_criteriaitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='criteriaItem',
        ),
        migrations.AddField(
            model_name='criteria',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='criterias', to='semesters.project'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CriteriaItem',
        ),
    ]
