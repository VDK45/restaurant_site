from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re

'''
class MenuForms(forms.Form):  # Формы не связаны с models
    name = forms.CharField(max_length=255, label='Tên menu', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Giới thiệu về menu', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5   # высота поля
    }))
    price = forms.IntegerField(label='Giá', widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))
    is_published = forms.BooleanField(label='Hiện menu', initial=True)

    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Loại menu',
                                      empty_label='Chọn loại menu: ', widget=forms.Select(attrs={
            "class": "form-control"
        }))  # queryset обязательный
'''


class MenuForms(forms.ModelForm):
    class Meta:
        model = Menu
        # fields = '__all__'
        fields = ['name', 'description', 'price', 'photo', 'is_published', 'category']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"}),
            'is_published': forms.NullBooleanSelect(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Ten khong the bat dau tu chu duoc')
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Gia khong the it hon 0')
        return price




