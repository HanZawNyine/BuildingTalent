# Generated by Django 3.0.14 on 2022-01-10 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update',
            new_name='updated',
        ),
    ]
