# Generated by Django 5.0.6 on 2025-02-27 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_remove_apply_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='job',
        ),
    ]
