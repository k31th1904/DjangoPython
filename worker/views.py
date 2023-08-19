from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import *
#from .forms import *
from .decorators import *
from django.contrib import messages
from datetime import date

@worker_required
def list_myassignments(request):

    # Get the employee object related to the current user
    employee = Employees.objects.get(user_id=request.user.id)

    # Get the assignments related to the employee and not claimed (claimed=0)
    assignments = Assignment.objects.filter(employee=employee, claimed=0)

    return render(request, 'MyAssignments.html', {'assignments': assignments})


# Claim (generate claim record) by trigger on assignment items
@worker_required
def claim(request, assignment_id):
    assignment = get_object_or_404(Assignment, assignment_id=assignment_id)
    #employee = Employees.objects.get(user_id=request.user.id)

    # Calculate the payment amount
    payment_amount = assignment.hours * assignment.salary_hour

    # Create a new claim object with the specified fields
    claim = Claims(
        assignment=assignment,
        approved="Pending",
        claim_date=date.today(),
        payment_amount=payment_amount,
        #processed_by="",
    )
    # Save the object
    claim.save()

    # Set claimed to true
    assignment.claimed = 1
    assignment.save()

    messages.success(request, 'Claim submitted successfully.')
    return HttpResponseRedirect('/wk/myassignments/')


@worker_required
def list_myclaims(request):
    # Get the employee object related to the current user
    employee = Employees.objects.get(user_id=request.user.id)

    # Render records related to the employee
    claims = Claims.objects.filter(assignment__employee=employee)
    return render(request, 'MyClaims.html', {'claims': claims})