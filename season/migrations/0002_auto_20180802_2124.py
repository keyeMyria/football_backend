# Generated by Django 2.1 on 2018-08-02 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='division',
            old_name='espn_id',
            new_name='leagueId',
        ),
    ]