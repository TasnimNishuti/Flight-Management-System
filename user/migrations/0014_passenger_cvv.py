# Generated by Django 2.1.5 on 2021-01-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_passenger_expiration'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='cvv',
            field=models.IntegerField(null=True),
        ),
    ]