from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.models import Group


# List Employees
def list_employees(request):
    employees = Employees.objects.all()
    return render(request, 'Employees.html', {"employees": employees})

# Add Employee (Disabled / Not used)
def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            employee = Employees(
                fname=form.cleaned_data['fname'],
                lname=form.cleaned_data['lname'],
                telephone=form.cleaned_data['telephone'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
            )
            employee.save()
            return HttpResponseRedirect('/sa/employees/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = AddEmployeeForm()
        return render(request, 'AddEmployee.html', {'form': form})

# Edit Employee
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            employee.fname = form.cleaned_data['fname']
            employee.lname = form.cleaned_data['lname']
            employee.telephone = form.cleaned_data['telephone']
            employee.address = form.cleaned_data['address']
            employee.email = form.cleaned_data['email']
            employee.save()
            employee.user.groups.clear()
            employee.user.groups.add(group)
            return HttpResponseRedirect('/sa/employees/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = AddEmployeeForm(initial={
            'fname': employee.fname,
            'lname': employee.lname,
            'telephone': employee.telephone,
            'address': employee.address,
            'email': employee.email,
            'group': employee.user.groups.first(),
        })
        return render(request, 'EditEmployee.html', {'form': form})


# Delete Employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    user = employee.user
    if request.method == "POST":
        employee.delete()
        # Also delete Django user table record
        user.delete()
        return redirect('list_employees')




############### Client Categories ###############

def list_clientcategories(request):
    categories = ClientCategories.objects.all()
    return render(request, 'ClientCategories.html', {'categories': categories})

def add_clientcategory(request):
    if request.method == 'POST':
        form = ClientCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clientcategories')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = ClientCategoryForm()
    return render(request, 'AddClientCategories.html', {'form': form})

def edit_clientcategory(request, category_id):
    category = get_object_or_404(ClientCategories, pk=category_id)
    if request.method == 'POST':
        form = ClientCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_clientcategories')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = ClientCategoryForm(instance=category)
    return render(request, 'EditClientCategories.html', {'form': form})

def delete_clientcategory(request, category_id):
    category = get_object_or_404(ClientCategories, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_clientcategories')


