# Generated by Django 4.0.4 on 2022-04-19 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0005_criteriaitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteriaitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='criteriaitem',
            name='weight',
        ),
        migrations.AddField(
            model_name='criteriaitem',
            name='criteria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='criteria.criteria'),
            preserve_default=False,
        ),
    ]
