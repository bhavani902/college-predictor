# Generated by Django 2.2 on 2019-09-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_predictor', '0002_auto_20190909_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cse',
            name='home_state',
        ),
        migrations.RemoveField(
            model_name='cse',
            name='name',
        ),
        migrations.AddField(
            model_name='college',
            name='home_state',
            field=models.CharField(blank=True, choices=[('IIT', 'IIT'), ('chhattisgarh', 'chhattisgarh'), ('rajasthan', 'rajasthan'), ('gujrat', 'gujrat'), ('karnataka', 'karnataka'), ('goa', 'goa')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='name',
            field=models.CharField(default='Computer Science and Engineering', max_length=200, null=True),
        ),
    ]
