# Generated by Django 4.0.5 on 2022-06-16 00:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('event_to_join', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.event')),
            ],
        ),
    ]
