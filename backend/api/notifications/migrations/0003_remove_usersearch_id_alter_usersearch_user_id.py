# Generated by Django 4.0.10 on 2023-04-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_usersearch_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersearch',
            name='id',
        ),
        migrations.AlterField(
            model_name='usersearch',
            name='user_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
