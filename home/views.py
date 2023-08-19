from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import EmployeeSignupForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView




# Show Home
def home(request):
    return render(request, 'home.html')


# Sign Up function
def user_signup(request):
    if request.method == 'POST':
        form = EmployeeSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = EmployeeSignupForm()
    return render(request, 'Signup.html', {'form': form})

# Login function
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # check if user exists in database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'invaliduser.html')

        # authenticate user with password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # redirect occur here so that they access pages based on their roles ####
            if user.groups.filter(name='system_admin').exists():
                return HttpResponseRedirect('/sa/')
            elif user.groups.filter(name='project_manager').exists():
                return HttpResponseRedirect('/pm/')
            elif user.groups.filter(name='worker').exists():
                return HttpResponseRedirect('/wk/')
            elif user.groups.filter(name='account_manager').exists():
                return HttpResponseRedirect('/am/')
            else:
                return render(request, 'invalidgroup.html')

        else:
            return render(request, 'invalidpw.html')

    return render(request, 'Login.html')

def user_logout(request):
    # clear session data
    #request.session.flush()

    # log out the user
    logout(request)

    #request.user.id = None

    return redirect('home')

# Show Permission Error
def permissionerror(request):
    return render(request, 'invalidpermission.html')


# Show Invalid Group Error
def invalidgrouperror(request):
    return render(request, 'invalidpermission.html')