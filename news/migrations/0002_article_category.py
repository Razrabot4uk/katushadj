# Generated by Django 5.0.4 on 2024-06-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='General', max_length=100),
        ),
    ]