from django import forms
from datetime import date
from .models import *
from django.contrib.auth.models import Group


class AddClientForm(forms.Form):
    cname = forms.CharField(label='Client Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label='Client Category', queryset=ClientCategories.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Telephone', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))



class AddProjectForm(forms.Form):
    client = forms.ModelChoiceField(label='Client', queryset=Clients.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    project_code = forms.CharField(label='Project Code', max_length=45, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_created = forms.DateField(label='Date Created',initial=date.today, required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

class AddAssignmentForm(forms.Form):
    TASK_CHOICES = [
        ('Remote', 'Remote'),
        ('On-Site', 'On-Site'),
    ]
    #Filter only worker will be shown, get object and then apply .objects.filter foreign key query
    worker_group = Group.objects.get(name='worker')
    employee = forms.ModelChoiceField(label='Employee', queryset=Employees.objects.filter(user__groups=worker_group), widget=forms.Select(attrs={'class': 'form-control'}))
    project = forms.ModelChoiceField(label='Project Code', queryset=Projects.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    task_date = forms.DateField(label='Assignment Date',initial=date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hours = forms.IntegerField(label='Hours', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    task_type = forms.ChoiceField(label='Task Type', choices=TASK_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    salary_hour = forms.IntegerField(label='Salary Per Hour', widget=forms.NumberInput(attrs={'class': 'form-control'}))