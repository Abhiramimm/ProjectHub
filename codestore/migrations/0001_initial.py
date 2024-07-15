# Generated by Django 5.0.6 on 2024-07-09 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('github_link', models.URLField()),
                ('image', models.ImageField(blank=True, default='project_images/default.jpg', null=True, upload_to='project_images')),
                ('project_preview', models.FileField(blank=True, null=True, upload_to='project_videos')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codestore.project')),
            ],
        ),
    ]