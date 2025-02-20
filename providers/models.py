# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    contact_email = models.EmailField(db_index=True)
    standard_crayon_price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)]
    )
    premium_crayon_price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)]
    )
    eco_friendly_crayon_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)]
    )
    offers_bulk_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Crayon Provider"
        verbose_name_plural = "Crayon Providers"
        ordering = ["name"]