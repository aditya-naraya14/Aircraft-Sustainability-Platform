from django.urls import re_path
import aircraft.views as part_view


urlpatterns = [
    re_path(r'^get_parts$', part_view.part_list),
    re_path(r'^aircraft_model$', part_view.aircraft_list),
    re_path(r'^get_data$', part_view.get_values_to_display)
]