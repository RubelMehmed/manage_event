# Generated by Django 3.2.5 on 2023-01-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=25, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Web Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=25, verbose_name='Zip Code'),
        ),
    ]
