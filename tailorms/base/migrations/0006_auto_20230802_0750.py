# Generated by Django 3.1.2 on 2023-08-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20230717_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='wallet',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
    ]
