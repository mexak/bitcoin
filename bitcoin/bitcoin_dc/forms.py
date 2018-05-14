from .models import Address
from django.forms import ModelForm


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
