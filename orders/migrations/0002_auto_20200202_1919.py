# Generated by Django 3.0 on 2020-02-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(blank=True, max_length=64)),
                ('toppings_amount', models.CharField(blank=True, max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_list', models.ManyToManyField(related_name='dishes', to='orders.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.AddField(
            model_name='dish',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes_containing', to='orders.Menu'),
        ),
        migrations.AddField(
            model_name='dish',
            name='toppings_list',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Topping'),
        ),
    ]