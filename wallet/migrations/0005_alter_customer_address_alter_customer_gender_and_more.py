# Generated by Django 4.0.6 on 2022-08-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]