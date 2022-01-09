# Generated by Django 3.1.14 on 2022-01-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
