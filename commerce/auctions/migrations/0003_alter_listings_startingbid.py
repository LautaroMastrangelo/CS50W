# Generated by Django 5.1.7 on 2025-04-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='startingBid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
