# Generated by Django 4.0.5 on 2022-06-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_join_joinevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]