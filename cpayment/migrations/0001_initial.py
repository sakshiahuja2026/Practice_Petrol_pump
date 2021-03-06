# Generated by Django 3.2.4 on 2021-06-29 04:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creditor_master', '0002_alter_creditor_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')])),
                ('type', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel')], default='petrol', max_length=30)),
                ('bankname', models.CharField(max_length=30)),
                ('branchname', models.CharField(max_length=30)),
                ('chequeno', models.IntegerField(max_length=16)),
                ('chequedate', models.DateField()),
                ('reference', models.CharField(max_length=50)),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpayment', to='creditor_master.creditor')),
            ],
        ),
    ]
