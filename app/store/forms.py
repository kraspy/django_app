from django import forms

from .models import Category, Product

TEXTINPUT_CLASSES = 'block w-full mb-2 rounded-md bg-white/5 px-3 py-1.5 text-base outline-1 -outline-offset-1 outline-white/10 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500'


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = (
            'name',
            'description',
            'price',
            'category',
            'status',
        )
        labels = {
            'name': 'Title',
            'description': 'Description',
            'price': 'Price',
            'category': 'Category',
            'status': 'Status',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': TEXTINPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': TEXTINPUT_CLASSES}),
            'price': forms.NumberInput(attrs={'class': TEXTINPUT_CLASSES}),
            'category': forms.Select(attrs={'class': TEXTINPUT_CLASSES}),
            'status': forms.Select(attrs={'class': TEXTINPUT_CLASSES}),
        }


class RemoveProductForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label='Do you really want to remove?',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'col-start-1 row-start-1 appearance-none rounded-sm border border-white/10 bg-white/5 checked:border-indigo-500 checked:bg-indigo-500 indeterminate:border-indigo-500 indeterminate:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500 disabled:border-white/5 disabled:bg-white/10 disabled:checked:bg-white/10 forced-colors:appearance-auto',
                'id': 'confirm',
            }
        ),
    )
