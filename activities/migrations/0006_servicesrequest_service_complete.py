# Generated by Django 4.1.1 on 2022-11-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_admitedpatitent_is_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesrequest',
            name='service_complete',
            field=models.BooleanField(default=False),
        ),
    ]
