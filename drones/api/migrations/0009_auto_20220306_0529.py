# Generated by Django 3.2.12 on 2022-03-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_drone_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='model',
            field=models.CharField(choices=[('LI', 'Ligthweight'), ('MI', 'Middleweight'), ('CR', 'Cruiseweight'), ('HW', 'Heavyweight')], default='LI', help_text='The model type of the drone', max_length=2),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('ID', 'IDLE'), ('LA', 'LOADING'), ('LO', 'LOADED'), ('DI', 'DELIVERING'), ('DE', 'DELIVERED'), ('RE', 'RETURNING')], default='ID', help_text='The current state of the drone', max_length=2),
        ),
    ]
