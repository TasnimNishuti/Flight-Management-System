# Generated by Django 2.1.5 on 2021-01-05 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210106_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_id',
        ),
    ]