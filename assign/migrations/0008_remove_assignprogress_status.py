# Generated by Django 4.1 on 2022-08-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("assign", "0007_assignprogress"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assignprogress",
            name="status",
        ),
    ]