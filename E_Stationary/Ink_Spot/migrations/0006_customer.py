# Generated by Django 4.1.3 on 2023-03-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0005_b_categories_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]