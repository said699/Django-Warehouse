from django import forms
from .models import Organization


class OrganizationRegisterForm(forms.ModelForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите ваш пароль'}))
    
    class Meta:
        model = Organization
        fields = ('inn', 'password1', 'password2', 'name', 'phone', 'currency', 'website', 'logo', 'address')

    def save(self, commit=True):
        organization = super().save(commit=False)
        organization.username = None
        organization.set_password(self.cleaned_data["password1"])
        if commit:
            organization.save()
        return organization
    
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data
