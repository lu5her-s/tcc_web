# Generated by Django 4.0.6 on 2022-08-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0002_alter_announce_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
