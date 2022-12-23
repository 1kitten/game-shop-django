from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Postal Code'
        self.fields['city'].widget.attrs['placeholder'] = 'City'

        for field in ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city'):
            self.fields[field].widget.attrs['class'] = 'input-reg'
            self.fields[field].help_text = ''
            self.fields[field].label = ''
