# Generated by Django 5.1.6 on 2025-02-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
