from django.shortcuts import render
from autoload.models import DumpTruck, TruckModel
from .utils import get_truck_models_list, get_tucks_by_selected_model


def main(request):
    truck_models_list = get_truck_models_list()
    selected_model = '-1'

    if request.method == "POST":
        selected_model = request.POST.get('trucklist')
        dump_truck_list = get_tucks_by_selected_model(selected_model)
    else:
        dump_truck_list = get_tucks_by_selected_model(selected_model)

    return render(request,
                  "index.html",
                  {
                    "truck_models_list": truck_models_list,
                    "dump_trucks": dump_truck_list,
                    "selected_model": int(selected_model),
                  }
                  )
