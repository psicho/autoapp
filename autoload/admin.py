from django.contrib import admin
from autoload.models import DumpTruck, TruckModel


@admin.register(DumpTruck)
class DumpTruckAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'side_number']


@admin.register(TruckModel)
class TruckModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'load_capacity']
