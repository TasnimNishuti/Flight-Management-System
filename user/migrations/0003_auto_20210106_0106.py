# Generated by Django 2.1.5 on 2021-01-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210106_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_id',
            field=models.TextField(default='717', null=True),
        ),
    ]
