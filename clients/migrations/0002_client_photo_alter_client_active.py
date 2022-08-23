# Generated by Django 4.1 on 2022-08-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]