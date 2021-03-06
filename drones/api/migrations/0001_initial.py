# Generated by Django 3.2.12 on 2022-03-04 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('model', models.PositiveSmallIntegerField(choices=[(1, 'Ligthweight'), (2, 'Middleweight'), (3, 'Cruiseweight'), (4, 'Heavyweight')], default=1, help_text='The model type of the drone')),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'IDLE'), (2, 'LOADING'), (3, 'LOADED'), (4, 'DELIVERING'), (5, 'DELIVERED'), (6, 'RETURNING')], default=1, help_text='The current state of the drone')),
                ('serial_number', models.CharField(help_text='The serial number of the drones', max_length=100, unique=True)),
                ('weight_limit', models.DecimalField(decimal_places=2, help_text='The weight limit that a dron can carry', max_digits=10)),
                ('battery_capacity', models.IntegerField(default=100, help_text='The percent capacity of the battery')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('image', models.ImageField(help_text='The image of the med', upload_to='meds')),
                ('weight', models.DecimalField(decimal_places=2, help_text='The weight in gr of the med', max_digits=10)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('drone_carrier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medication', to='api.drone')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='drone',
            name='medications',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drones', to='api.medication'),
        ),
    ]
