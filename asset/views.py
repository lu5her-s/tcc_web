from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.core import serializers
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from asset.forms import AssetForm

from asset.models import (
    Asset,
)

# Create your views here.

class AssetListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'asset/asset.html'
    model = Asset
    ordering = ('-created_at')
    
class AssetDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'asset/asset_detail.html'
    model = Asset

class AssetCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'asset/asset_form.html'
    form_class = AssetForm
    success_url = reverse_lazy('asset:list')

    def get(self, request, *args, **kwargs):
        context = {
            'form' : self.form_class,
            'title' : 'Create',
            'header' : 'เพิ่มรายการทรัพย์สิน',
            'btn_text' : 'เพิ่ม'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            form = self.form_class()
        context = {
            'form' : form,
        }
        return render(request, self.template_name, context)

class AssetUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'asset/asset_form.html'
    form_class = AssetForm
    model = Asset
    # success_url = reverse_lazy('asset:detail', kwargs={'pk' : self.pk})

    def get_success_url(self):
        return reverse_lazy('asset:detail', kwargs={'pk' : self.get_object().pk })
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        context = {
            'form' : form,
            'header' : 'แก้ไชสินทรัพย์',
            'title' : 'Update',
            'btn_text' : 'อัพเดท',
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        else:
            form = self.form_class(instance=self.get_object())
            context = {
                'form' : form,
                'header' : 'แก้ไชสินทรัพย์',
                'title' : 'Update',
                'btn_text' : 'อัพเดท',
            }
        return render(request, self.template_name, context)
        

class AssetDeleteView(LoginRequiredMixin, DeleteView):
    model = Asset
    template_name = 'asset/asset_delete.html'
    success_url = reverse_lazy('asset:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Delete'
        context["header"] = "ลบสินทรัพย์"
        context["btn_text"] = "ยืนยันการลบ"
        return context
    


