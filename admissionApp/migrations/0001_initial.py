# Generated by Django 3.2.8 on 2021-12-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('firstName', models.CharField(max_length=40)),
                ('middleName', models.CharField(default='', max_length=40)),
                ('lastName', models.CharField(default='', max_length=40)),
                ('motherName', models.CharField(max_length=40)),
                ('fatherName', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
