from django import forms
from cars.models import Car
    

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor mínimo é de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'A data de fabricação deve ser a partir de 1975')
        return factory_year
