# Generated by Django 3.1.14 on 2022-01-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0010_auto_20220109_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
