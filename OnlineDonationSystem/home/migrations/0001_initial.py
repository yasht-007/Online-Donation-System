# Generated by Django 3.2.2 on 2021-05-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundCollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]
