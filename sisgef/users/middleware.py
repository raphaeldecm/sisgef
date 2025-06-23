import datetime
from django.conf import settings
from django.shortcuts import redirect

class SessionIdleTimeout:
    """
    Expira sessão após X segundos de inatividade.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        now = datetime.datetime.utcnow()
        last = request.session.get('last_touch')
        timeout = getattr(settings, 'SESSION_IDLE_TIMEOUT', 1800)

        if last and (now - datetime.datetime.fromisoformat(last)).total_seconds() > timeout:
            from django.contrib.auth import logout
            logout(request)
            return redirect('login')

        request.session['last_touch'] = now.isoformat()
        return self.get_response(request)