from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from asset.forms import AssetForm

from asset.models import (
    Asset,
)

# Create your views here.

class AssetListView(LoginRequiredMixin, ListView):
    template_name = 'asset/asset.html'
    model = Asset
    ordering = ('-created_at')
    
class AssetDetailView(LoginRequiredMixin, DetailView):
    template_name = 'asset/asset_detail.html'
    model = Asset

class AssetCreateView(LoginRequiredMixin, CreateView):
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