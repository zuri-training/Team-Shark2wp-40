
from django.urls import include, path
# from .views import *
from . import views
# SchoolAccount
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    # path("profile/", userProfile, name="userProfile"), 
    # path("school_reg/", schoolRegView, name="schoolRegView"),
    path("school_profile/", views.schoolProfile, name="schoolprofile"),
    path("guardian_profile/", views.guardianProfile, name="guardianprofile"),
   
]

