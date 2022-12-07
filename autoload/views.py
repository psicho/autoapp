from .utils import get_truck_models_list, get_tucks_by_selected_model
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "index.html"
    truck_models_list = get_truck_models_list()

    def get_context_data(self, *, object_list=None, **kwargs):
        truck_models_list = get_truck_models_list()
        selected_model = '-1'
        dump_truck_list = get_tucks_by_selected_model(selected_model)
        context = {
            "truck_models_list": truck_models_list,
            "dump_trucks": dump_truck_list,
            "selected_model": int(selected_model)
        }
        return context

    def post(self, request):
        truck_models_list = get_truck_models_list()
        selected_model = request.POST.get('trucklist')
        dump_truck_list = get_tucks_by_selected_model(selected_model)
        context = {
            "truck_models_list": truck_models_list,
            "dump_trucks": dump_truck_list,
            "selected_model": int(selected_model)
        }
        return self.render_to_response(context)

