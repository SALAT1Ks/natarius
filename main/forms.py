# myapp/forms.py
from django import forms

class UserInputForm(forms.Form):
    phone_input = forms.CharField(
        label='',
        max_length=18,
        widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'type': "tel",
            'name': 'phone',
            'id': 'phone_input',
            'placeholder' : 'Введите ваш номер телефона',
            'data-phone-pattern': '+7 (___) ___-__-__',
            'style': 'font-size: 1.2rem;'
        })
    )
    fio_input = forms.CharField(
        label='',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваше ФИО',
            'class': 'custom-input',
            'style': 'font-size: 1.1rem;'
        })
    )
