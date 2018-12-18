# Generated by Django 2.1.4 on 2018-12-18 13:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_server', '0003_auto_20181218_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubdivisionManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('patronymic_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('employment_date', models.DateField(default=None)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'verbose_name': 'SubdivisionManager',
                'verbose_name_plural': 'SubdivisionManagers',
            },
        ),
        migrations.AlterField(
            model_name='manager',
            name='employee',
            field=models.ManyToManyField(related_name='employee', to='employee_server.Employee'),
        ),
        migrations.AddField(
            model_name='subdivisionmanager',
            name='manager',
            field=models.ManyToManyField(related_name='manager', to='employee_server.Manager'),
        ),
        migrations.AddField(
            model_name='subdivisionmanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subdivisionmanager', related_query_name='subdivisionmanager', to=settings.AUTH_USER_MODEL),
        ),
    ]
