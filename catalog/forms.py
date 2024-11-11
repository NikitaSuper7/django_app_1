from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'videos']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'выберите изображение'
        })
        self.fields['videos'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_description(self):
        description = self.cleaned_data.get('description')
        spam_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']

        if description and any(item in description.lower() for item in spam_words):
            raise ValidationError("В описании продукта присутствуют запрещенные слова")
        return description

    def clean_name(self):
        name = self.cleaned_data.get('name')
        spam_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']

        if name and any(item in name.lower() for item in spam_words):
            raise ValidationError("В названии продукта присутствуют запрещенные слова")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError("Стоимость не может быть меньше 0")
        return price



