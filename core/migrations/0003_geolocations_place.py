# Generated by Django 3.2.9 on 2021-11-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_geolocations_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocations',
            name='place',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
