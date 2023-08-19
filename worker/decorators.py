from functools import wraps
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect


def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/permissionerror/')
        return _wrapped_view
    return decorator


worker_required = group_required('worker')
