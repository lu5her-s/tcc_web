from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)

from journal.models import Journal, JournalImage
from journal.forms import JournalForm

# Create your views here.

class JournalListView(LoginRequiredMixin, ListView):
    template_name = 'journal/journal.html'
    model         = Journal
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        qs = Journal.objects.filter(author=self.request.user)
        return qs

class JournalCreateView(LoginRequiredMixin, CreateView):
    template_name = 'journal/journal_form.html'
    # model = Journal
    form_class = JournalForm
    success_url = reverse_lazy('journal:list')
    login_url = reverse_lazy('login')
    
    def get(self, request, *args, **kwargs):
        context = {
           'form' : self.form_class,
           'title' : 'Create',
           'header' : 'ทึกการปฏิบัติงาน',
           'btn_text' : 'Save Work' 
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            images = request.FILES.getlist('images')
            form_save = form.save()
            form_id = get_object_or_404(Journal, pk=form_save.pk)
            
            if images:
                for image in images:
                    a_image = JournalImage(journal=form_id, images=image)
                    a_image.save()
            else:
                form_save.save()
                
            return redirect(self.success_url)
        else:
            form = self.form_class()
            
        context = {
            'form' : form,
            'title' : 'Create',
            'header': 'บึนทึกการปฏิบัติงาน',
            'btn_text' : 'Save Work'
        }
        return render(request, self.template_name, context)

class JournalDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'journal/journal_detail.html'
    model = Journal
    
    def get_context_data(self, **kwargs):
        context = super(JournalDetailView, self).get_context_data(**kwargs)
        context['images'] = JournalImage.objects.filter(journal=self.object)
        
        return context