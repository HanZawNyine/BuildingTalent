# Generated by Django 3.1.14 on 2022-01-09 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0007_remove_comment_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jade.customer'),
        ),
    ]