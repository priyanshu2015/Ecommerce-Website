# Generated by Django 3.0.5 on 2020-10-03 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in proper format in 10 digits.', regex='^\\+?1?\\d{10}$')]),
        ),
    ]