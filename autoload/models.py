from django.db import models


class TruckModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    load_capacity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class DumpTruck(models.Model):
    name = models.CharField(max_length=100, blank=True)
    model = models.ForeignKey(
        TruckModel,
        on_delete=models.CASCADE,
        related_name='dumptruck'
    )
    side_number = models.CharField(max_length=30, unique=True, blank=True)
    current_load = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=None)

    def __str__(self):
        return f"Самосвал №{self.side_number}, модель {self.model}"
