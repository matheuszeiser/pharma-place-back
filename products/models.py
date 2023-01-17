from django.db import models
import uuid


class CategoriesName(models.TextChoices):
    SAUDE = "Saúde"
    BELEZA = "Beleza"
    COSMETICOS = "Cosméticos"
    HIGIENE = "Higiene"
    MEDICAMENTOS = "Medicamentos"
    INFALTIL = "Infaltil"
    CONVENIENCIA = "Conveniência"


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    image = models.URLField()
    category = models.CharField(max_length=50, choices=CategoriesName.choices)
    price = models.DecimalField()

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="product"
    )
