# Generated by Django 4.0.4 on 2022-04-24 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evalutaion', '0001_initial'),
        ('judge', '0003_judge_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='evaluation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evalutaion.evaluation'),
        ),
    ]
