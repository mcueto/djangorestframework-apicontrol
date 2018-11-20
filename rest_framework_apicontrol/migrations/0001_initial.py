# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.URLField(blank=True, null=True)),
                ('api_key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationalUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationalUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=30)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_framework_apicontrol.App')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='rest_framework_apicontrol.OrganizationalUnitType')),
            ],
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='organizationalunit',
            name='responsibles',
            field=models.ManyToManyField(to='rest_framework_apicontrol.Responsible'),
        ),
        migrations.AddField(
            model_name='organizationalunit',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='rest_framework_apicontrol.OrganizationalUnitType'),
        ),
    ]