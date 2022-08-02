# Generated by Django 4.0.6 on 2022-07-30 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('gender', models.CharField(max_length=8)),
                ('age', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=8)),
                ('nationality', models.CharField(max_length=2)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile pics')),
                ('employment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
                ('pin', models.TextField(default='', max_length=12)),
                ('history', models.DateTimeField()),
                ('Customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]