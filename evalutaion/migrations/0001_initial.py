# Generated by Django 4.0.4 on 2022-04-24 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semesters', '0016_project_criterias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semesters.project')),
            ],
        ),
    ]
