# Generated by Django 5.0 on 2023-12-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='albums',
            name='Songs_artist',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
