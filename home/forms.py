from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employees

"""
 Created a form make use of two models, one is the Django built in User model 
 and the other one is our customized employee model 
"""
class EmployeeSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(max_length=12, label='Contact No.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=45, label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'telephone', 'address', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control form-input'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control form-input'}),
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        employee = Employees(user=user,
                             fname=self.cleaned_data['first_name'],
                             lname=self.cleaned_data['last_name'],
                             telephone=self.cleaned_data['telephone'],
                             address=self.cleaned_data['address'],
                             email=self.cleaned_data['email'])
        employee.save()
        return user
