# Generated by Django 3.1.14 on 2021-12-30 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jade', '0005_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jade.product')),
            ],
        ),
    ]