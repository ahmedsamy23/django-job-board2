# Generated by Django 5.0.6 on 2025-02-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_apply_created_at_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
