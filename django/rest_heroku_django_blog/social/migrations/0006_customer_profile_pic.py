# Generated by Django 4.0.1 on 2022-01-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_customer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
