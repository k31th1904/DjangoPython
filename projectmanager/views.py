from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import *
from .decorators import *
from .forms import *




# List Clients
@project_manager_required
def list_clients(request):
    clients=Clients.objects.all()
    return render(request, 'Clients.html', {"clients":clients})

# Add Client
@project_manager_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = Clients(
                cname=form.cleaned_data['cname'],
                category=form.cleaned_data['category'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
                address=form.cleaned_data['address'],
            )
            client.save()
            return HttpResponseRedirect('/pm/clients/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest()
            # We can use HttpResponseRedirect here to notify user and redirect for further user action
    else:
        form = AddClientForm()
        return render(request, 'AddClient.html', {'form': form})

# Edit Client
@project_manager_required
def edit_client(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client.cname = form.cleaned_data['cname']
            client.category = form.cleaned_data['category']
            client.email = form.cleaned_data['email']
            client.telephone = form.cleaned_data['telephone']
            client.address = form.cleaned_data['address']
            client.save()
            return HttpResponseRedirect('/pm/clients/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = AddClientForm(initial={
            'cname': client.cname,
            'category': client.category,
            'email': client.email,
            'telephone': client.telephone,
            'address': client.address,
        })
        return render(request, 'EditClient.html', {'form': form})

# Delete Client
@project_manager_required
def delete_client(request, client_id):
    client = get_object_or_404(Clients, client_id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('list_clients')


#################################Projects###################################

# List Projects
@project_manager_required
def list_projects(request):
    projects = Projects.objects.all()
    return render(request, 'Projects.html', {"projects": projects})

# Add Project
@project_manager_required
def add_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            project = Projects(
                client=form.cleaned_data['client'],
                project_code=form.cleaned_data['project_code'],
                description=form.cleaned_data['description'],
                date_created=form.cleaned_data['date_created'],
                project_mang=Employees.objects.get(user=request.user),
            )
            project.save()
            return HttpResponseRedirect('/pm/projects/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = AddProjectForm()
        return render(request, 'AddProject.html', {'form': form})

# Edit Project
@project_manager_required
def edit_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            project.client = form.cleaned_data['client']
            project.project_code = form.cleaned_data['project_code']
            project.description = form.cleaned_data['description']
            project.save()
            return HttpResponseRedirect('/pm/projects/')
        else:
            print("Form errors:", form.errors)
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = AddProjectForm(initial={
            'client': project.client,
            'project_code': project.project_code,
            'description': project.description,
            'date_created': project.date_created,
        })
        return render(request, 'EditProject.html', {'form': form})

# Delete Project
@project_manager_required
def delete_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('list_projects')


#################### Project Assignments #####################
@project_manager_required
def list_assignments(request):
    assignments = Assignment.objects.all()
    return render(request, 'ProjectAssignment.html', {'assignments': assignments})

@project_manager_required
def add_assignment(request):
    if request.method == 'POST':
        form = AddAssignmentForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            project = form.cleaned_data['project']
            task_date = form.cleaned_data['task_date']
            hours = form.cleaned_data['hours']
            task_type = form.cleaned_data['task_type']
            salary_hour = form.cleaned_data['salary_hour']

            assignment = Assignment(employee=employee,
                                    project=project,
                                    task_date=task_date,
                                    hours=hours,
                                    task_type=task_type,
                                    salary_hour=salary_hour,
                                    claimed=0)
            assignment.save()
            return redirect('list_assignments')
    else:
        form = AddAssignmentForm()
    return render(request, 'AddAssignment.html', {'form': form})

@project_manager_required
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('list_assignments')
    return render(request, 'DeleteAssignment.html', {'assignment': assignment})