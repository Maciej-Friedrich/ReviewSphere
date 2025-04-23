from flask_login import current_user
from functools import wraps
from flask import abort

def is_admin():
    return current_user.is_authenticated and current_user.role == 'admin'

def is_moderator():
    return current_user.is_authenticated and current_user.role == 'moderator'

def is_reviewer():
    return current_user.is_authenticated and current_user.role == 'recenzent'

def can_edit_or_delete(item):
    return (
        current_user.is_authenticated and (
            item.user_id == current_user.id or
            current_user.role in ['admin', 'moderator']
        )
    )

def permission_required(check_func):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not check_func():
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator