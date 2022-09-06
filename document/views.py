#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : views.py
# Author            : lu5her <lu5her@mail>
# Date              : Sat Sep, 03 2022, 18:45 246
# Last Modified Date: Sat Sep, 03 2022, 21:09 246
# Last Modified By  : lu5her <lu5her@mail>
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
from document.forms import DocumentForm
from document.models import Accept, Document


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'document/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inbox'] = Document.objects.filter(assigned_group=self.request.user.profile.sector)
        context['outbox'] = Document.objects.filter(author__profile__sector__id=self.request.user.profile.sector.id)
        context['to_me'] = Document.objects.filter(assigned_to=self.request.user.profile)
        context['all-inbox'] = Document.objects.all()
        #context['to_sector'] = Inbox.objects.filter(assigned_group=self.request.user.profile.sector)
        return context

class DocumentAllView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Document
    template_name = 'document/document.html'

class InboxListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Document
    template_name = 'document/inbox.html'

    def get_queryset(self):
        qs = Document.objects.filter(assigned_group=self.request.user.profile.sector)
        return qs

class InboxDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Document
    template_name = 'document/inbox_detail.html'

    def post(self, *args, **kwargs):
        document = self.get_object()
        user = self.request.user
        accepted = Accept(
                document=document,
                user=user
                )
        accepted.save()
        return render(request, self.template_name, {})

class OutboxListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Document
    template_name = 'document/outbox.html'

    def get_queryset(self):
        qs = Document.objects.filter(author__profile__sector__id = self.request.user.profile.sector.id)
        return qs

class OutBoxDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Document
    template_name = 'document/outbox_detail.html'

class OutboxCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Document
    form_class = DocumentForm
    template_name = 'document/document_form.html'
    success_url = reverse_lazy('document:outbox')
