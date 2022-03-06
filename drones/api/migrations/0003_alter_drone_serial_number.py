# Generated by Django 3.2.12 on 2022-03-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_drone_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(help_text='The serial number of the drones', max_length=100, unique=True),
        ),
    ]