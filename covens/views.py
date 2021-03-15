from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Coven


class CovenListView(ListView):
    template_name = "covens/coven_list.html"
    model = Coven


class CovenDetailView(DetailView):
    template_name = "covens/coven_detail.html"
    model = Coven


class CovenCreateView(CreateView):
    template_name = "covens/coven_create.html"
    model = Coven
    fields = []


class CovenUpdateView(UpdateView):
    template_name = "covens/coven_update.html"
    model = Coven
    fields = []


class CovenDeleteView(DeleteView):
    template_name = "covens/coven_delete.html"
    model = Coven
    success_url = reverse_lazy("coven_list")