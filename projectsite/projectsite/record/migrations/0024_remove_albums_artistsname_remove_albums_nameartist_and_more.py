# Generated by Django 5.0 on 2024-01-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0023_artist_nameofartist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='ArtistsName',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='NameArtist',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='nameofartist',
        ),
        migrations.AlterField(
            model_name='artist',
            name='Artist_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
