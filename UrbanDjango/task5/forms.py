from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label="Введите логин", max_length=30, required=True)
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput, min_length=8, required=True)
    repeat_password = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, min_length=8, required=True)
    age = forms.IntegerField(label="Введите свой возраст", required=True, min_value=0, max_value=120)
