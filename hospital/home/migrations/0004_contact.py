# Generated by Django 4.1.3 on 2022-12-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=10)),
            ],
        ),
    ]