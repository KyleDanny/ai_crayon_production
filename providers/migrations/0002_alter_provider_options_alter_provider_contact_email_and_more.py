# Generated by Django 5.1.6 on 2025-02-19 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="provider",
            options={
                "ordering": ["name"],
                "verbose_name": "Crayon Provider",
                "verbose_name_plural": "Crayon Providers",
            },
        ),
        migrations.AlterField(
            model_name="provider",
            name="contact_email",
            field=models.EmailField(db_index=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="provider",
            name="eco_friendly_crayon_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="name",
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="provider",
            name="premium_crayon_price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="standard_crayon_price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
