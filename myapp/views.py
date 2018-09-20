from django.shortcuts import render
from .models import Users
from django.views.generic import TemplateView,CreateView
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .form import UserForm


class WelcomeView(TemplateView):
    template_name = 'myapp/welcome.html'


class UserListView(generic.ListView):
    template_name = 'myapp/list.html'
    context_object_name = 'userlist'

    def get_queryset(self):
        return Users.objects.raw('SELECT * FROM myapp_users')

class CreateUserView(CreateView):
    form_class = UserForm
    http_method_names = ('post', 'get')
    template_name = 'myapp/new_user.html'
    success_url = reverse_lazy('myapp:list')