# Generated by Django 4.0.6 on 2022-08-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_rename_assettype_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='request_able',
            field=models.BooleanField(default=True),
        ),
    ]
