
from django.urls import include, path
from .views import *
from . import views
# SchoolAccount
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    # path("profile/", userProfile, name="userProfile"), 
    # path("school_reg/", schoolRegView, name="schoolRegView"),
    path("dashboard/", login_required(ListDebtor.as_view()), name="dashboard"),
    # path("dashboard/", views.dashBoard, name="dashboard"),
    path("guardian_profile/", views.guardianProfile, name="guardianprofile"),
    # path('dashboard/<int:id>/', login_required(DetailDebtor.as_view()), name='detail-debtor'),
   
]

