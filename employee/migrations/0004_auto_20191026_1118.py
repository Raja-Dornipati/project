# Generated by Django 2.2.4 on 2019-10-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20191024_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
