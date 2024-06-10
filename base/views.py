from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.conf import settings

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import credential
from .forms import PositionForm

from cryptography.fernet import Fernet
from django_password_eye.fields import PasswordEye

import base64


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('credentials')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('credentials')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('credentials')
        return super(RegisterPage, self).get(*args, **kwargs)


class credentialList(LoginRequiredMixin, ListView):
    model = credential
    context_object_name = 'credentials'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['credentials'] = context['credentials'].filter(user=self.request.user)
        context['count'] = context['credentials'].filter(owned=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['credentials'] = context['credentials'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class CredentialDetail(LoginRequiredMixin, DetailView):
    model = credential
    # context_object_name = 'credential'
    
    template_name = 'base/credential.html'
    


class CredentialCreate(LoginRequiredMixin, CreateView):
    model = credential
    fields = ['title', 'username', 'password']
    success_url = reverse_lazy('credentials')

    def form_valid(self, form):
        form.instance.user = self.request.user

        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(form.cleaned_data['password'].encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
        
        form.instance.password = encrypt_pass

        return super(CredentialCreate, self).form_valid(form)


class CredentialUpdate(LoginRequiredMixin, UpdateView):
    model = credential
    password = PasswordEye(label='')
    fields = ['title', 'username', 'password', 'last_updated']

    def get_object(self, queryset=None):
        credential = super(CredentialUpdate, self).get_object(queryset=queryset)
        
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        pas = base64.urlsafe_b64decode(credential.password)
        decoded_pass = cipher_pass.decrypt(pas).decode('ascii')
        
        credential.password = decoded_pass
        print(credential.password)
        return credential

    success_url = reverse_lazy('credentials')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = credential
    context_object_name = 'credential'
    success_url = reverse_lazy('credentials')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class CredentialReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_credential_order(positionList)

        return redirect(reverse_lazy('credentials'))
