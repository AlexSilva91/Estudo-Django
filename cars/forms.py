from django import forms
from cars.models import Brand, Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser maior que R$ 20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar veículo de fabricação anterior a 1975!')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        
        if photo is None:
            self.add_error('photo', 'Não é possível cadastrar carro sem foto!')
        return photo