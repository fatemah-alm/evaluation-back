# Generated by Django 4.0.4 on 2022-04-25 00:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_judge_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]