from django import forms
from .models import *
from django.contrib.auth.models import Group



class AddEmployeeForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=45, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(label='Last Name', max_length=45, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Telephone', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=45, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class EditEmployeeForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    lname = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Telephone', max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    group = forms.ModelChoiceField(label='Role', queryset=Group.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class ClientCategoryForm(forms.ModelForm):
    class Meta:
        model = ClientCategories
        fields = ['category_name']
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category_name': 'Category Name',
        }



class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

