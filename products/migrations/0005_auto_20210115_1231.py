# Generated by Django 3.1.5 on 2021-01-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210115_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.CharField(max_length=50, verbose_name='Ürün Adedi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ürün Görseli'),
        ),
    ]