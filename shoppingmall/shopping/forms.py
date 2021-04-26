from django import forms 
from shopping.models import Shopping

class ShoppingForm(forms.ModelForm):

    class Meta:
        model = Shopping
        fields = '__all__' #(to show all fields)
        # exclude = ['name'] #(if dont want show name) 

        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'product name'
            }),
            'brand' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'product brand'
            }),
            # 'description' : forms.Textarea(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : 'product description'
            # }),
            'price' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'product price',
                'type' : 'number'
            }),
            'cover' : forms.FileInput(attrs={
                'class' : 'form-control'
            })
        }