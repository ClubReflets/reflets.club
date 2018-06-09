from functools import wraps
from flask import session, redirect, url_for

class Auth(object):
    def login_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user' not in session:
                return redirect(url_for('/'))
            return f(*args, **kwargs)
        return decorated_function