# Generated by Django 3.2.12 on 2022-03-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220306_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='model',
            field=models.CharField(choices=[('Ligthweight', 'Ligthweight'), ('Middleweight', 'Middleweight'), ('Cruiseweight', 'Cruiseweight'), ('Heavyweight', 'Heavyweight')], default='Ligthweight', help_text='The model type of the drone', max_length=12),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], default='IDLE', help_text='The current state of the drone', max_length=12),
        ),
    ]
