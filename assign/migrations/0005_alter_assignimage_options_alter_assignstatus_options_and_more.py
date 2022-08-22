# Generated by Django 4.0.6 on 2022-08-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('assign', '0004_alter_assign_body_alter_assign_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignimage',
            options={'verbose_name': 'Images', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='assignstatus',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='assign',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='account.profile'),
        ),
    ]
