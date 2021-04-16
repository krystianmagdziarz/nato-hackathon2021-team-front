# Generated by Django 3.2 on 2021-04-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_x', models.CharField(blank=True, max_length=2, null=True, verbose_name='X position on the map')),
                ('grid_y', models.CharField(blank=True, max_length=2, null=True, verbose_name='Y position on the map')),
                ('range', models.IntegerField(blank=True, null=True, verbose_name='Range')),
            ],
        ),
    ]
