# Generated by Django 4.1.1 on 2022-11-19 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_alter_diagnosticreport_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosticreport',
            name='patient',
        ),
    ]
