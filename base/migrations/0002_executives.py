# Generated by Django 4.0.5 on 2022-06-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('exexcutive_pos', models.CharField(max_length=200, null=True)),
                ('whatsapp_url', models.CharField(max_length=200, null=True)),
                ('facebook_url', models.CharField(max_length=200, null=True)),
                ('instagram_url', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
