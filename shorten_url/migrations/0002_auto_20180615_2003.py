# Generated by Django 2.0.6 on 2018-06-15 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_url', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weburl',
            old_name='shot_url',
            new_name='short_url',
        ),
    ]
