from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Seller

class SellerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Seller
        fields = ('email', 'name', 'phone', 'address')


class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Введите Email'}))

class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'email', 'phone', 'address')

    def clean_email(self):
        email = self.cleaned_data.get(email)
        if Seller.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Этот email уже используется!')
        return email