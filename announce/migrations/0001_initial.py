# Generated by Django 4.0.6 on 2022-07-30 05:32

import announce.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announce')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AnnounceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=announce.models.get_image_name)),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announce')),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to=announce.models.get_file_name)),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announce.announce')),
            ],
        ),
        migrations.AddField(
            model_name='announce',
            name='is_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_type', to='announce.announcetype'),
        ),
        migrations.AddField(
            model_name='announce',
            name='reads',
            field=models.ManyToManyField(related_name='readers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announce',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_status', to='announce.announcestatus'),
        ),
    ]
