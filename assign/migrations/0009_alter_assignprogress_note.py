# Generated by Django 4.1 on 2022-08-21 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assign", "0008_remove_assignprogress_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignprogress",
            name="note",
            field=models.TextField(),
        ),
    ]
