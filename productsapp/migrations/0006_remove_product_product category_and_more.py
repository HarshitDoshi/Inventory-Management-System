# Generated by Django 4.0 on 2022-01-06 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0005_remove_product_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Product Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product Supplier',
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productsapp.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productsapp.supplier'),
            preserve_default=False,
        ),
    ]