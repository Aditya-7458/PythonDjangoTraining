from django import forms

class MyForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    