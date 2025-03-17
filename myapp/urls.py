from django.urls import path
import myapp.views as views

urlpatterns = [
    path("log-in/", views.log_in, name="log-in"),
    path("log-out/", views.log_out, name="log-out"),
    path("get-user/", views.get_user, name="get-user"),
]
