# Generated by Django 2.1.5 on 2021-01-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_passenger_pay_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='name_card',
            field=models.TextField(null=True),
        ),
    ]
