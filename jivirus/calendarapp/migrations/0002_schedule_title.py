# Generated by Django 4.2.5 on 2023-10-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='title',
            field=models.CharField(default='Default Title', max_length=30),
        ),
    ]
