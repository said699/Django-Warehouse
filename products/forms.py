from django import forms
from django.utils import timezone
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price_of_one', 'count',  'manufacturer', 'created_at', 'description', 'is_active', 'image']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        } 

    def clean_created_at(self):
        created = self.cleaned_data.get('created_at')
        if created and created > timezone.localdate():
            raise forms.ValidationError('Дата выпуска не может быть в будущем!')
        return created