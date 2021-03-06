# Generated by Django 3.2.4 on 2021-06-28 13:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_master', '0003_rename_accountno_employee_bankaccountno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ifsccode',
        ),
        migrations.AddField(
            model_name='employee',
            name='IFSCcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
    ]
