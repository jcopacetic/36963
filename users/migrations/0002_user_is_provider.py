# Generated by Django 3.1.2 on 2020-10-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_provider',
            field=models.BooleanField(default=True),
        ),
    ]
