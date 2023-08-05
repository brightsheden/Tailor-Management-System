# Generated by Django 3.1.2 on 2023-06-22 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_customer_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.fashioncompany'),
        ),
        migrations.AlterField(
            model_name='work',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='base.customer'),
        ),
        migrations.AlterField(
            model_name='work',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='style', to='base.style'),
        ),
        migrations.AlterField(
            model_name='work',
            name='tailor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tailor', to='base.tailor'),
        ),
    ]