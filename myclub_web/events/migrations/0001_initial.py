# Generated by Django 3.2.5 on 2023-01-11 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('zip_code', models.CharField(max_length=25, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=25, verbose_name='Phone')),
                ('web', models.URLField(verbose_name='Web Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateField(auto_now_add=True)),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, null=True, to='events.MyClubUser')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]
