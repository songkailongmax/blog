# Generated by Django 2.1 on 2020-08-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='total_views_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
