# Generated by Django 4.0.1 on 2022-01-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/%Y/%m/%d'),
        ),
    ]
