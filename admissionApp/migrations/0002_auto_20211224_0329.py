# Generated by Django 3.2.8 on 2021-12-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='middleName',
            field=models.CharField(max_length=40),
        ),
    ]
