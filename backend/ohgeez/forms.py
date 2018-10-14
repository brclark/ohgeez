from django.forms import ModelForm

from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'address', 'city', 'state', 'zip_code',
            'phone_number', 'description', 'category',)
