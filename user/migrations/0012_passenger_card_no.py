# Generated by Django 2.1.5 on 2021-01-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_passenger_name_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='card_no',
            field=models.IntegerField(null=True),
        ),
    ]