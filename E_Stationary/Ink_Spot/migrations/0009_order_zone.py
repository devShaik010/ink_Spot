# Generated by Django 4.1.7 on 2023-06-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0008_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
