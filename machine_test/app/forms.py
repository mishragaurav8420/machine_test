from django import forms
from .models import User,Product
class SelectProductForm(forms.Form):
    user_name=forms.CharField( max_length=255)
    # products=forms.MultipleChoiceField(=[1,2,3],widget=forms.CheckboxSelectMultiple)
    product=forms.ModelChoiceField()
    