from django import forms
from .models import Category


class MenuForms(forms.Form):
    name = forms.CharField(max_length=255, label='Tên menu', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Giới thiệu về menu', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5   # высота поля
    }))
    price = forms.IntegerField(label='Giá', widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))
    is_published = forms.BooleanField(label='Hiện menu', initial=True, widget=forms.NullBooleanSelect(attrs={
        "class": "form-control"
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Loại menu',
                                      empty_label='Chọn loại menu: ', widget=forms.Select(attrs={
            "class": "form-control"
        }))  # queryset обязательный



