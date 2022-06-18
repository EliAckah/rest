# Generated by Django 4.0.5 on 2022-06-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_executives_executive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_title', models.CharField(max_length=200, null=True)),
                ('cause_detail', models.CharField(max_length=200, null=True)),
                ('cause_pic', models.ImageField(default='avatar.svg', null=True, upload_to='')),
            ],
        ),
    ]