from django.urls import path
from .views import *
from account import views


app_name ='school'
login_required(DetailDebtor.as_view())
urlpatterns = [
    # path("dashboard/", views.dashBoard, name="dashboard"),
    path("dashboard/", login_required(ListDebtor.as_view()), name="dashboard"),
    path("add_debtor/", login_required(CreateDebtor.as_view()), name="add-debtor"),
    path('dashboard/<int:id>/', login_required(DetailDebtor.as_view()), name='detail-debtor'),
    path("add_schadmin/", login_required(CreateSchoolAdmin.as_view()), name="add-schadmin"),
    path("add_message/", CreateMessage.as_view(), name="add-message"),
    path("delete_schadmin/", login_required(CreateSchoolAdmin.as_view()), name="delete-schadmin"),
    # path("view_debtor/", ListDebtor.as_view(), name="view-debtor"),
    path("", landingPage, name="landingpage"),
    path("contact", contactPage, name="contactpage"),
    path("faq", faqPage, name="faqpage"),
    path("about", aboutPage, name="aboutpage"),

  
]