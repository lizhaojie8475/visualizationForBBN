# Generated by Django 3.0.1 on 2020-01-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='authority',
            field=models.CharField(default='read', max_length=16),
        ),
    ]
