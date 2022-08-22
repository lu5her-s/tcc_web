# Generated by Django 4.0.6 on 2022-08-15 03:18

import assign.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=assign.models.get_image_name)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign.assign')),
            ],
        ),
    ]
