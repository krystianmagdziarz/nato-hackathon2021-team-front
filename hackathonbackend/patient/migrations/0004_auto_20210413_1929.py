# Generated by Django 3.2 on 2021-04-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20210413_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='grid_x',
            field=models.CharField(max_length=2, verbose_name='X position on the map'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grid_y',
            field=models.CharField(max_length=2, verbose_name='Y position on the map'),
        ),
    ]
