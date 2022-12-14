# Generated by Django 4.0.6 on 2022-08-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=600)),
                ('transaction_description', models.CharField(max_length=26)),
                ('transaction_amount', models.BigIntegerField()),
                ('transaction_charge', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=30)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination', to='wallet.wallet')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_origin', to='wallet.wallet')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
    ]
