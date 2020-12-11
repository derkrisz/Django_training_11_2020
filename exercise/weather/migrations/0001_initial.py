# Generated by Django 3.1.3 on 2020-12-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=260, null=True)),
                ('temperature', models.FloatField(default=20.0)),
            ],
        ),
    ]
