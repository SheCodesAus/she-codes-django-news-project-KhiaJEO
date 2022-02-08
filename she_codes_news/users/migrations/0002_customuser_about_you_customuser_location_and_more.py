# Generated by Django 4.0.1 on 2022-02-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='About_you',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Your_socials',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.URLField(blank=True),
        ),
    ]