# Generated by Django 2.2.3 on 2019-07-12 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190712_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='city',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='message',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='state',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='street1',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='street2',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='zip',
        ),
    ]