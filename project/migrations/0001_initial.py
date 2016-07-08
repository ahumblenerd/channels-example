# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-07 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('owners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('projectManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Project_Manager', to=settings.AUTH_USER_MODEL)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Chat_room', to='chat.Room')),
            ],
        ),
    ]
