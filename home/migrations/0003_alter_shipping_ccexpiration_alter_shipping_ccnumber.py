# Generated by Django 4.1.3 on 2022-12-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_shipping_credit_remove_shipping_debit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shipping",
            name="ccExpiration",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="shipping",
            name="ccNumber",
            field=models.CharField(max_length=19),
        ),
    ]
