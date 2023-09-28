from django.urls import path
from useraccount.views import user_login, user_logout, signup, user_profile, add_profile, view_profile
app_name = "user"
urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup, name="signup"),
    path("user_profile/", user_profile, name="user_profile"),
    path("add_profile/", add_profile, name="add_profile"),
    path("view_profile/<str:username>/", view_profile, name="view_profile"),
]