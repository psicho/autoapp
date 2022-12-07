from autoload.models import DumpTruck, TruckModel


def get_truck_models_list() -> list:
    truck_models = TruckModel.objects.all()
    truck_models_list = [
        {
            "name": model.name,
            "id": model.id,
        } for model in truck_models
    ]
    truck_models_list.insert(0, {"id": "-1", "name": "ВСЕ"})
    return truck_models_list


def get_tucks_by_selected_model(selected_model: str) -> list:
    selected_trucks = DumpTruck.objects.select_related('model')
    if selected_model != '-1':
        selected_trucks = selected_trucks.filter(model=selected_model)
    selected_trucks = [
        {
            "side_number": truck.side_number,
            "model": truck.model.name,
            "capacity": truck.model.load_capacity,
            "current_load": truck.current_load,
            "overload": calc_capacity_reload(truck.current_load, truck.model.load_capacity),
        } for truck in selected_trucks
    ]
    return selected_trucks


def calc_capacity_reload(current_load: float, over_load: float) -> int:
    return int(current_load / over_load * 100) - 100
