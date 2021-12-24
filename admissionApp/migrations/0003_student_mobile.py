# Generated by Django 3.2.8 on 2021-12-23 22:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionApp', '0002_auto_20211224_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)]),
            preserve_default=False,
        ),
    ]
