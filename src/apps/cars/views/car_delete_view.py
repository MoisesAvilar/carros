from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from cars.models import Car
from django.views.generic import DeleteView


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):

    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
