from cars.models import Car
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from cars.forms import CarModelForm


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):

    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
