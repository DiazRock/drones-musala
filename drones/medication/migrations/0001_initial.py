# Generated by Django 3.2.12 on 2022-03-01 04:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drone_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('image', models.ImageField(upload_to='meds')),
                ('weight', models.IntegerField(help_text='The weight in gr of the med')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message="Allowed\xa0only\xa0letters,\xa0numbers,\xa0'-',\xa0'_'", regex='^[a-zA-Z0-9_-]+$')])),
                ('code', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message="Allowed\xa0only\xa0letters,\xa0numbers,\xa0'-',\xa0'_'", regex='^[A-Z0-9_]+$')])),
                ('drone_carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_model.drone')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
