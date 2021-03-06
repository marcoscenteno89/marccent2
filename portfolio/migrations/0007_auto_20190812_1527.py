# Generated by Django 2.2.4 on 2019-08-12 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190809_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='address',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='email',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='email',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='date_created',
        ),
        migrations.AddField(
            model_name='address',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='address',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Updated'),
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Updated'),
        ),
        migrations.AddField(
            model_name='email',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='email',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Updated'),
        ),
        migrations.AddField(
            model_name='phone',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='phone',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Updated'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='address',
            name='lng',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Street 2'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5, verbose_name='Zip Code'),
        ),
    ]
