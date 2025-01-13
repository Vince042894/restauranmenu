from django.utils.translation.template import context_re
from django.views import generic
from django.views.generic import DetailView

from .models import Item, MEAL_TYPE

class Menulist(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(DetailView):
    model = Item
    template_name = "menu_detail.html"