# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('home', '0005_urbanblogindexpagerelatedlink_urbanblogpagerelatedlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanBlogPagesTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='commonblogspagestag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='commonblogspagestag',
            name='tag',
        ),
        migrations.AlterField(
            model_name='urbanblogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='home.UrbanBlogPagesTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='CommonBlogsPagesTag',
        ),
        migrations.AddField(
            model_name='urbanblogpagestag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='home.UrbanBlogPage'),
        ),
        migrations.AddField(
            model_name='urbanblogpagestag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_urbanblogpagestag_items', to='taggit.Tag'),
        ),
    ]