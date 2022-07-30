from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
    )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from account.models import (
    Profile,
    Sector,
    Rank,
    Position,
    LineToken
    )
from account.forms import (
    LineTokenForm,
    UserCreateForm,
    UserForm,
    ProfileForm
    )
# Create your views here.

class RegisterView(CreateView):
    ''' for user registration '''
    form_class = UserCreationForm
    # form_class = UserCreateForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'registration/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    ''' for update member'''
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('account:profile')
    
    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(self.success_url)
        else:
            context = {
                'user_form' : UserForm(request.POST, instance=request.user),
                'profile_form' : ProfileForm(request.POST, instance=request.user.profile)
            }
            
        return render(request, self.template_name, context)

    def get(self, request):
        context = {
            'user_form' : UserForm(instance=request.user),
            'profile_form' : ProfileForm(instance=request.user.profile)
        }
        return render(request, self.template_name, context)
        
class PasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    model = User
    template_name = 'registration/password_change.html'

class MemberListView(ListView):
    template_name = 'registration/member_list.html'
    queryset = User.objects.all()
    paginate_by = 10
    # REVIEW : User.objects.all().exclude(is_superuser=True)

class MemberDetailView(LoginRequiredMixin, DetailView):
    template_name = 'registration/profile.html'
    model = User
    
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {
            'user' : user
        }
        return render(request, self.template_name, context)

class LineTokenListView(LoginRequiredMixin, ListView):
    template_name = 'registration/line_token.html'
    model = LineToken
    paginate_by = 10

class LineTokenCreateView(LoginRequiredMixin, CreateView):
    model = LineToken
    template_name = 'registration/line_token_form.html'
    form_class = LineTokenForm
    success_url = reverse_lazy('account:line-token')
    
    def get_context_data(self, **kwargs):
        context = super(LineTokenCreateView, self).get_context_data(**kwargs)
        context["title"] = "Create"
        context["header"] = "เพิ่ม Line Token"
        context["btn_text"] = "เพิ่ม Token"
        return context
    
class LineTokenUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/line_token_form.html'
    model = LineToken
    form_class = LineTokenForm

    # def get_context_data(self, **kwargs):
    #     context = super(LineTokenUpdateView, self).get_context_data(**kwargs)
    #     context["title"] = "Update"
    #     context["header"] = "อัพเดท Line Token"
    #     context["btn_text"] = "อัพเดท Token"
    #     return context
   
    
    def get(self, request, pk):
        line_token = LineToken.objects.get(pk=pk)
        form = self.form_class(instance=line_token)
        context = {
            'form' : form,
            'title' : 'Update',
            'header' : "Update",
            'btn_text' : "อัพเดท Token"
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        line_token = LineToken.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=line_token)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            form = self.form_class(instance=line_token)
            context = {
                'form' : form
            }
            return render(request, self.template_name, context)
        
        