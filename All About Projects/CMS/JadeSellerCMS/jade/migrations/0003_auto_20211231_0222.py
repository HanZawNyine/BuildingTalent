# Generated by Django 3.1.14 on 2021-12-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0002_auto_20211231_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
