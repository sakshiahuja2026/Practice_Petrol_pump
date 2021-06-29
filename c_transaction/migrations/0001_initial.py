# Generated by Django 3.2.4 on 2021-06-29 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('nozzel_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('petrol', models.IntegerField()),
                ('diesel', models.IntegerField()),
                ('pp', models.IntegerField()),
                ('dp', models.IntegerField()),
                ('nozzel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nozzel', to='nozzel_master.nozzel')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='vehicle.vehicle')),
            ],
        ),
    ]
