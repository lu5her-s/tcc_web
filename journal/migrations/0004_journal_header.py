# Generated by Django 4.0.6 on 2022-08-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_rename_type_journal_is_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
