# Generated by Django 4.0.6 on 2022-08-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_customer_address_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=54)),
                ('symbol', models.CharField(max_length=12)),
                ('amount', models.BigIntegerField()),
            ],
        ),
    ]
