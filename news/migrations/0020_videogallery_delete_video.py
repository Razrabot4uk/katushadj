# Generated by Django 5.0.4 on 2024-09-25 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_announcement_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/', verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='news.event')),
            ],
            options={
                'verbose_name': 'Видео галерея',
                'verbose_name_plural': 'Видео галереи',
            },
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
