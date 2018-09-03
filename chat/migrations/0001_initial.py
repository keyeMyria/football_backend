# Generated by Django 2.1 on 2018-09-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=3000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
