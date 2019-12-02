from django import forms
from .models import CustomerData

class CreationForm(forms.Form):
    customer_id = forms.IntegerField(
        label='Enter Customer Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Customer Id'
            }
        )
    )

    customer_name = forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Customer Name'
            }
        )
    )

    customer_mobile = forms.IntegerField(
        label='Enter Customer Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Customer Mobile Number'
            }
        )
    )

    customer_email = forms.EmailField(
        label='Enter Customer Email Id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Customer Email Id'
            }
        )
    )

    product_id = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Id'
            }
        )
    )

    product_name = forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Name'
            }
        )
    )

    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Cost'
            }
        )
    )

    Number_of_products = forms.IntegerField(
        label='Enter Number of products',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Number of products'
            }
        )
    )

class UpdationForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product Name',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Id'
            }
        )
    )

    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Cost'
            }
        )
    )

class DeletionForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product Name',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Id'
            }
        )
    )

