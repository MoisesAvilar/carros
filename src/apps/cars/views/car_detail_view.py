from cars.models import Car
from django.views.generic import DetailView


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
