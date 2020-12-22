from django.views import generic

from . import forms, models


class CarListView(generic.ListView):
    model = models.Car
    form_class = forms.CarForm


class CarCreateView(generic.CreateView):
    model = models.Car
    form_class = forms.CarForm


class CarDetailView(generic.DetailView):
    model = models.Car
    form_class = forms.CarForm


class CarUpdateView(generic.UpdateView):
    model = models.Car
    form_class = forms.CarForm
    pk_url_kwarg = "pk"


class MakeListView(generic.ListView):
    model = models.Make
    form_class = forms.MakeForm


class MakeCreateView(generic.CreateView):
    model = models.Make
    form_class = forms.MakeForm


class MakeDetailView(generic.DetailView):
    model = models.Make
    form_class = forms.MakeForm


class MakeUpdateView(generic.UpdateView):
    model = models.Make
    form_class = forms.MakeForm
    pk_url_kwarg = "pk"
