# Generated by Django 4.2.6 on 2024-05-17 13:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^\\+\\d{1,3} \\(\\d{3}\\) \\d{3}-\\d{4}$')]),
        ),
    ]
