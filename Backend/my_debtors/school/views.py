from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import *
from .models import *


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )

# Landing page View

def landingPage(request):

    context = {}
    return render(request, 'index.html', context)


def aboutPage(request):

    context = {}
    return render(request, 'about.html', context)

def contactPage(request):

    context = {}
    return render(request, 'contact.html', context)

def faqPage(request):

    context = {}
    return render(request, 'FAQs.html', context)


# @login_required(login_url='login')

# def dashBoard(request):

#     context = {}
#     return render(request, 'school/dashboard.html', context)

# School Admin Views

class CreateSchoolAdmin(CreateView):
    template_name = 'school/add_admin.html'
    form_class    = SchoolAdminForm
    queryset      = SchoolAdmin.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('school:dashboard')


class ListSchoolAdmin(ListView):
    template_name = 'school/school.html'
    queryset = SchoolAdmin.objects.all()

class DetailSchoolAdmin(DetailView):
    template_name = 'school/school.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SchoolAdmin, id=id_)

class UpdateSchoolAdmin(UpdateView):
    template_name = 'school/school.html'
    form_class    = SchoolAdminForm
    queryset      = SchoolAdmin.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SchoolAdmin, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DeleteSchoolAdmin(DeleteView):
    template_name = 'school/school.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SchoolAdmin, id=id_)

    def get_success_url(self):
        return reverse('school:view-debtor')


# Debtors Views

class CreateDebtor(CreateView):
    template_name = 'school/add_debtor.html'
    form_class    = DebtorForm
    queryset      = Debtor.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('school:dashboard')


class ListDebtor(ListView):
    template_name = 'school/dashboard.html'
    queryset = Debtor.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Debtor, id=id_)


class DetailDebtor(DetailView):
    template_name = 'school/delete_debtor.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Debtor, id=id_)

class UpdateDebtor(UpdateView):
    template_name = 'school/delete_debtor.html'
    form_class    = DebtorForm
    queryset      = Debtor.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Debtor, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DeleteDebtor(DeleteView):
    template_name = 'school/delete_debtor.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Debtor, id=id_)

    def get_success_url(self):
        return reverse('school:dashboard')

# message/ comment Views

class CreateMessage(CreateView):
    template_name = 'school/add_message.html'
    form_class    = MessageForm
    queryset      = Message.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('school:landingpage')


class ListMessage(ListView):
    template_name = 'school/school.html'
    queryset = SchoolAdmin.objects.all()

class DetailMessage(DetailView):
    template_name = 'school/school.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Message, id=id_)

class UpdateMessage(UpdateView):
    template_name = 'school/school.html'
    form_class    = MessageForm
    queryset      = Message.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Message, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DeleteMessage(DeleteView):
    template_name = 'school/school.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Message, id=id_)

    def get_success_url(self):
        return reverse('school:view-debtor')

