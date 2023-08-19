
from django.db import models
from django.contrib.auth.models import User


class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    task_date = models.DateField()
    hours = models.IntegerField()
    task_type = models.CharField(max_length=20, blank=True, null=True)
    salary_hour = models.IntegerField()
    claimed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Claims(models.Model):
    claim_id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(Assignment, models.DO_NOTHING, db_column='assignment')
    approved = models.CharField(max_length=20, blank=True, null=True)
    claim_date = models.DateField()
    payment_amount = models.IntegerField(blank=True, null=True)
    processed_by = models.ForeignKey('Employees', models.DO_NOTHING, db_column='processed_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claims'



class ClientCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = False
        db_table = 'client_categories'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    email = models.CharField(max_length=45)
    telephone = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=100)
    category = models.ForeignKey(ClientCategories, models.DO_NOTHING)

    def __str__(self):
        return self.cname

    class Meta:
        managed = False
        db_table = 'clients'



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    # Own Employees table is 1to1 linked with Django built-in User table
    # We have to use related_name to prevent clashes between models from different app
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="projectmanger_employee")
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    telephone = models.CharField(max_length=12)
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'employees'


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    project_code = models.CharField(max_length=45)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    project_mang = models.ForeignKey(Employees, models.DO_NOTHING, db_column='project_mang')

    def __str__(self):
        return self.project_code

    class Meta:
        managed = False
        db_table = 'projects'



