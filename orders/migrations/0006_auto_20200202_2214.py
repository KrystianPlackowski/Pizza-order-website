# Generated by Django 3.0 on 2020-02-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200202_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='toppings_amount',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]