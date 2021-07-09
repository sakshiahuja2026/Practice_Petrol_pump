# Generated by Django 3.2.4 on 2021-07-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntransaction', '0002_auto_20210706_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ntransaction',
            old_name='dieselafter',
            new_name='card',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='petrolafter',
            new_name='cash',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='creditorslipno',
            new_name='creditoramount',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='dieselbefore',
            new_name='googlepay',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='petrolbefore',
            new_name='paytm',
        ),
        migrations.RemoveField(
            model_name='ntransaction',
            name='creditor_amount',
        ),
        migrations.RemoveField(
            model_name='ntransaction',
            name='reference_id',
        ),
        migrations.RemoveField(
            model_name='ntransaction',
            name='type',
        ),
        migrations.AddField(
            model_name='ntransaction',
            name='phonepay',
            field=models.FloatField(blank=True, null=True),
        ),
    ]