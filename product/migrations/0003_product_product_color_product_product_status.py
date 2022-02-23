# Generated by Django 4.0.2 on 2022-02-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
