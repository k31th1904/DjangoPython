from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .decorators import *
from django.contrib.auth.models import Group

# List Employees
@system_admin_required
def list_employees(request):
    employees = Employees.objects.all()
    return render(request, 'Employees.html', {"employees": employees})

# Add Employee (Disabled / Not used)
@system_admin_required
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
@system_admin_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    if request.method == 'POST':
        form = EditEmployeeForm(request.POST)
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
        form = EditEmployeeForm(initial={
            'fname': employee.fname,
            'lname': employee.lname,
            'telephone': employee.telephone,
            'address': employee.address,
            'email': employee.email,
            'group': employee.user.groups.first(),
        })
        return render(request, 'EditEmployee.html', {'form': form})

# Delete Employee
@system_admin_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    user = employee.user
    if request.method == "POST":
        employee.delete()
        # Also delete Django user table record
        user.delete()
        return redirect('list_employees')




############### Client Categories ###############
@system_admin_required
def list_clientcategories(request):
    categories = ClientCategories.objects.all()
    return render(request, 'ClientCategories.html', {'categories': categories})

@system_admin_required
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

@system_admin_required
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

@system_admin_required
def delete_clientcategory(request, category_id):
    category = get_object_or_404(ClientCategories, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_clientcategories')


############ Groups (Django Built-in) #########


@system_admin_required
def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'Groups.html', {'groups': groups})


@system_admin_required
def add_group(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            return HttpResponseRedirect('/sa/groups/')
        else:
            return HttpResponseBadRequest('Invalid group name')
    else:
        return render(request, 'AddGroup.html')


@system_admin_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect('/sa/groups/')
    else:
        return HttpResponseBadRequest('Invalid request method')