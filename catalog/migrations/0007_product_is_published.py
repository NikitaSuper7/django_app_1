# Generated by Django 5.1.1 on 2024-11-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_videos"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
