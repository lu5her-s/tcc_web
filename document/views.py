# type: ignore
from itertools import chain
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        TemplateView,
        UpdateView,
        )
# from account.models import Sector
from document.forms import InboxForm, OutboxForm

from document.models import Inbox, InboxFile, Outbox, OutboxFile

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'document/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inbox'] = Inbox.objects.all()
        context['to_me'] = Inbox.objects.filter(assigned_to=self.request.user.profile)
        context['to_sector'] = Inbox.objects.filter(assigned_group=self.request.user.profile.sector)
        context['outbox'] = Outbox.objects.all()
        return context


def to_me(request):
    qs = Inbox.objects.filter(assigned_to=request.user.profile)
    context = {
            'object_list': qs,
            'description': request.user,
            }
    return render(request, 'document/inbox.html', context)

def to_sector(request):
    qs1 = Inbox.objects.filter(assigned_group=request.user.profile.sector)
    qs2 = Outbox.objects.filter(send_to=request.user.profile.sector)
    qs = list(chain(qs1, qs2))
    context = {
            'object_list': qs,
            'sector' : request.user.profile.sector,
            }
    return render(request, 'document/inbox.html', context)

class InboxListView(LoginRequiredMixin, ListView):

    """For Inbox List view"""
    login_url = reverse_lazy('login')
    model = Inbox
    template_name = 'document/inbox.html'

    # def get_queryset(self):
        # qs1 = Inbox.objects.all()
        # qs2 = Outbox.objects.filter(send_to__name="ส่วนกลาง")
        # qs = list(chain(qs1, qs2))
        # return qs

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

class InboxUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Inbox
    template_name = 'document/inbox_form.html'
    form_class = InboxForm
    pk = None
    
    def get_success_url(self):
        return reverse_lazy('document:inbox-detail', kwargs={'pk': self.get_object().pk})

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        files = InboxFile.objects.filter(inbox=self.get_object())

        context = {
                'form': form,
                'files': files,
                'title': 'Update',
                'header': 'แก้ไขเอกสารขาออก',
                'btn_text': 'แก้ไข' 
                }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())

        if form.is_valid():
            files = request.FILES.getlist('files')
            form_save = form.save()
            form_id = get_object_or_404(Inbox, pk=form_save.pk)

            if files:
                for file in files:
                    try:
                        a_file = InboxFile.objects.get(inbox=form_id)
                        a_file.files = file
                        a_file.save()
                    except ObjectDoesNotExist:
                        a_file = InboxFile.objects.create(inbox=form_id, files=file)
                        a_file.save()

            else:
                form_save.save()

            return redirect(self.get_success_url())

        else:
            form = self.form_class(instance=self.get_object())

        return render(request, self.template_name, {'form': form})

class OutboxListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Outbox
    template_name = 'document/outbox.html'

class OutboxCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Outbox
    form_class = OutboxForm
    template_name = 'document/outbox_form.html'
    success_url = reverse_lazy('document:outbox')

    def get(self, request, *args, **kwargs):
        context = {
                'form': self.form_class,
                'title': 'Send Document',
                'header': 'หนังสือส่ง',
                'btn_text': 'Send',
                }
        return render(request, self.template_name, context) 

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('files')
            form_save = form.save()
            form_id = get_object_or_404(Outbox, pk=form_save.pk)

            if files:
                for file in files:
                    a_file = OutboxFile(outbox=form_id, files=file)
                    a_file.save()
            else:
                form_save.save()

            return redirect(self.success_url)

        else:
            form = self.form_class()

        context = {
                'form': self.form_class,
                'title': 'Send Outbox',
                'header': 'หนังสือส่ง',
                'btn_text': 'Send',
                }
        return render(request, self.template_name, context)
        return super().post(request, *args, **kwargs)

class OutboxDetailView(LoginRequiredMixin, DetailView):
    pass
