# Generated by Django 3.1.4 on 2021-01-13 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spotifytoken',
            old_name='tokent_type',
            new_name='token_type',
        ),
    ]
