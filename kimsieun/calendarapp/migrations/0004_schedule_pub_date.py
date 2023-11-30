# Generated by Django 4.2.5 on 2023-10-02 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_alter_schedule_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]