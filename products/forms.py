from django import forms
from django.utils import timezone
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'indeficator', 'price_of_one', 'currency', 'count',  'manufacturer', 'created_at', 'description', 'is_active', 'image')
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        } 

    def clean_created_at(self):
        created = self.cleaned_data.get('created_at')
        if created and created > timezone.localdate():
            raise forms.ValidationError('Дата выпуска не может быть в будущем!')
        return created
    
class ExitProducts(forms.Form):
    indeficator = forms.CharField(label='Индификатор')
    count = forms.IntegerField(min_value=1, label='Количество')

    def clean(self):
        cleaned_data = super().clean()
        indeficator = cleaned_data.get('indeficator')
        count = cleaned_data.get('count')
        
        try:
            product = Product.objects.get(indeficator=indeficator)
            self.product_instance = product
        except Product.DoesNotExist:
            raise forms.ValidationError('Товара с таким индефикатором нет!')
        
        if count > product.count:
            raise forms.ValidationError('Нету такого количества')
        
        return cleaned_data