from django.http import HttpRequest, HttpResponse
import uuid

users = {"admin": "password"}
sessions = {}

SESSION_COOKIE_NAME = "sessionid"


def session_middleware(func):
    def wrapper(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        set_cookie = False
        session_id = request.COOKIES.get(SESSION_COOKIE_NAME)
        if not session_id:
            set_cookie = True
            session_id = str(uuid.uuid4())
            sessions[session_id] = {}
        request.session = sessions[session_id]
        response = func(request, *args, **kwargs)
        if set_cookie:
            response.set_cookie(SESSION_COOKIE_NAME, session_id)
        return response

    return wrapper


@session_middleware
def log_in(request: HttpRequest) -> HttpResponse:
    user = request.GET.get("user")
    password = request.GET.get("password")

    if user in users and users[user] == password:
        request.session["user"] = user
        return HttpResponse("Successfully logged in")
    else:
        return HttpResponse("Log-in failed", status=401)


@session_middleware
def log_out(request: HttpRequest) -> HttpResponse:
    if "user" in request.session:
        del request.session["user"]
    return HttpResponse("Logged out")


@session_middleware
def get_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"User: {request.session.get('user', '(not logged in)')}")
