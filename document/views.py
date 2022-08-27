# type: ignore
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        TemplateView,
        )
from document.forms import InboxForm

from document.models import Inbox, InboxFile

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'document/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inbox'] = Inbox.objects.all()
        context['to_me'] = Inbox.objects.filter(assigned_to=self.request.user.profile)
        context['to_sector'] = Inbox.objects.filter(assigned_group=self.request.user.profile.sector)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('files')
            form_save = form.save()
            form_id = get_object_or_404(Inbox, pk=form_save.pk)

            if files:
                for file in files:
                    a_file = InboxFile(inbox=form_id, files=file)
                    a_file.save()
            else:
                form_save.save()

            return redirect(self.success_url)

        else:
            form = self.form_class()

        context = {
                'form' : self.form_class,
                'title' : 'Accept to Inbox',
                'header' : 'หนังสือรับ',
                'btn_text' : 'Accept to Inbox',
                }
        return render(request, self.template_name, context)

class InboxDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Inbox
    template_name = 'document/inbox_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = InboxFile.objects.filter(inbox=self.object)
        return context
