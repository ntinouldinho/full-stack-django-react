# Generated by Django 4.0.10 on 2023-04-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersearch',
            name='ip',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
