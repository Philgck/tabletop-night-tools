# Generated by Django 4.2.18 on 2025-01-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_addgame_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='addgame',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
