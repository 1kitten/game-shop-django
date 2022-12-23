from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'

        for field in ('username', 'first_name', 'last_name', 'password1', 'password2'):
            self.fields[field].widget.attrs['class'] = 'input-reg'
            self.fields[field].help_text = ''
            self.fields[field].label = ''


class BalanceForm(forms.Form):
    amount = forms.DecimalField(max_digits=100000, decimal_places=2, min_value=0)

    def __init__(self, *args, **kwargs):
        super(BalanceForm, self).__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs['class'] = 'decimal-balance'
        self.fields['amount'].label = ''
