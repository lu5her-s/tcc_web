# Generated by Django 4.1 on 2022-08-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
        ("document", "0003_inbox_assigned_group_inbox_assigned_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inbox",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignedUser",
                to="account.profile",
            ),
        ),
    ]
