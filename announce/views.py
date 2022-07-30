from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from announce.forms import AnnounceForm
from announce.models import Announce

# Create your views here.

class AnnounceListView(LoginRequiredMixin, ListView):
    model = Announce
    template_name = 'announce/announce.html'
    context_object_name = 'announce_list'
    paginate_by = 20
    ordering = ('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super(AnnounceListView, self).get_context_data(**kwargs)
        context['read'] = Announce.objects.filter(reads__id=self.request.user.id)
        context['header'] = "ประชาสัมพันธ์"
        return context
    
class AnnounceNotReadView(LoginRequiredMixin, ListView):
    model = Announce
    template_name = 'announce/announce.html'
    context_object_name = 'announce_list'
    paginate_by = 20
    ordering = ('-created_at')
    
    def get_queryset(self):
        # return super().get_queryset()
        qs = Announce.objects.filter(~Q(author=self.request.user) & ~Q(reads__id=self.request.user.id))
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(AnnounceNotReadView, self).get_context_data(**kwargs)
        context['not_read'] = self.request.user.announce_set.filter(~Q(author=self.request.user) & Q(reads__id=self.request.user.id)).count()
        context['header'] = "ยังไม่ได้อ่าน"
        return context
    
def announce_read(request, pk):
    announce = get_object_or_404(Announce, pk=request.POST.get('announce_id'))
    if announce.reads.filter(id=request.user.id).exists():
        announce.reads.remove(request.user)
    else:
        announce.reads.add(request.user)
    return HttpResponseRedirect(reverse_lazy('announce:detail', args=[str(pk)]))

class AnnounceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'announce/announce_form.html'
    form_class = AnnounceForm
    success_url = reverse_lazy('announce:list')
    
    def get(self, request, *args, **kwargs):
        context = {
            'form' : self.form_class
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            images = request.FILES.getlist('images')
            files = request.FILES.getlist('files')
            tokens = request.POST.getlist('tokens')
            form_save = form.save()