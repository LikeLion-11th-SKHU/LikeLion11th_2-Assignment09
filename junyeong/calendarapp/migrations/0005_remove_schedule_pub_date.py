# Generated by Django 4.2.5 on 2023-10-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_schedule_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='pub_date',
        ),
    ]
