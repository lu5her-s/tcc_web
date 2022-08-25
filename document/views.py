# type: ignore
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
        CreateView,
        ListView,
        TemplateView,
        )
from document.forms import InboxForm

from document.models import Inbox

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'document/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class InboxListView(LoginRequiredMixin, ListView):

    """For Inbox List view"""
    login_url = reverse_lazy('login')
    model = Inbox
    template_name = 'document/inbox.html'

class InboxCreateView(LoginRequiredMixin, CreateView):
    ''' For Accepted document to inbox '''
    login_url = reverse_lazy('login')
    model = Inbox
    form_class = InboxForm
    template_name = 'document/inbox_form.html'
    success_url = reverse_lazy('document:inbox')

    def get(self, request, *args, **kwargs):
        context = {
                'form' : self.form_class,
                'title' : 'Accept to Inbox',
                'header' : 'หนังสือรับ',
                'btn_text' : 'Accept to Inbox',
                }
        return render(request, self.template_name, context)
