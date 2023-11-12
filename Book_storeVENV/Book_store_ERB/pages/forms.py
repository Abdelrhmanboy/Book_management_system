from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'book_photo' : forms.FileInput(attrs={'class':'form-control'}),
            'author_photo' : forms.FileInput(attrs={'class':'form-control'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'monthly_rental_price' : forms.NumberInput(attrs={'class':'form-control' , 'id':'rentalPrice'}),
            'rental_period' : forms.NumberInput(attrs={'class':'form-control' , 'id':'rentalPeriod'}),
            'rental_total' : forms.NumberInput(attrs={'class':'form-control' , 'id':'rentalTotal'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
        }