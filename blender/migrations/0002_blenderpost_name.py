# Generated by Django 5.1.6 on 2025-02-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blenderpost',
            name='name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
