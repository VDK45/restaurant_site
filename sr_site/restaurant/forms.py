from django import forms
from django.forms import Textarea
from .models import *
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

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


# class CustomCaptchaTextInput(CaptchaTextInput):
#     template_name = 'custom_field.html'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Tên đăng nhập', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Xác nhận mật khẩu', widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                help_text='Xin bạn hãy dùng mật khẩu trên 8 ký tự!')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
        '''
        # Not working
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),

        }
        '''


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Tên đăng nhập', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 3})  # Form 5 dỏng

    class Meta:
        model = Comments
        fields = ('text',)




