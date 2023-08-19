from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .decorators import *
from .forms import *

# Create your views here.


@account_manager_required
def list_claims(request):
    # Only render pending records (not processed yet)
    claims = Claims.objects.filter(approved="Pending")
    return render(request, 'Claims.html', {'claims': claims})

@account_manager_required
def list_claimshistory(request):
    # Exclude pending records (processed)
    claims = Claims.objects.exclude(approved="Pending")
    return render(request, 'ClaimsHistory.html', {'claims': claims})

@account_manager_required
def approve_claim(request, claim_id):
    #get user object with current user ID
    employee = get_object_or_404(Employees, user=request.user)
    claim = get_object_or_404(Claims, claim_id=claim_id)
    claim.approved = "Approved"
    claim.processed_by = employee
    claim.save()
    return redirect('/am/claims/')

@account_manager_required
def deny_claim(request, claim_id):
    # get user object with current user ID
    employee = get_object_or_404(Employees, user=request.user)
    claim = get_object_or_404(Claims, claim_id=claim_id)
    claim.approved = "Rejected"
    claim.processed_by = employee
    claim.save()
    return redirect('/am/claims/')