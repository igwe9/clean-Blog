# Generated by Django 2.2.4 on 2019-12-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
