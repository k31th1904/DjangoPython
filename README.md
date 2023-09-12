Mini project - Simple Python app with MVT Django framework with MYSQL database.

Description:
Apps separation are role based and there are :
1. systemadmin - System Admin use case > ClientsCategories, Permission Groups, Employees Profile
2. projectmanager - Project Manager use case > Clients, Projects, Assignments
3. accountmanager - Account Manager use case > Claims
4. worker - Worker Employee > Assignments, Claims
5. home - Home (Landing) page control and redirection, User registration & authentication


Clean environment setup reminder:
In order to align employee ID (customized table) with user ID (Django built-in auth table),
we need to create an root/admin user from Signup page first, and then set is_staff, is_superuser = 1 from database.
So that we will have a superuser to access Django built-in admin page to initiate permission group and assignment 
(those are required from decorators.py), then we will be able to access different pages with group permission control assignment.

Brand-new environment setup:
1. Execute SQL statement to create table
2. Execute SQL statement to insert pre-usage data
3. Django settings.py to link up database
4. Django manage.py makemigrations
5. Django manage.py migrate
6. Start the app and play around
