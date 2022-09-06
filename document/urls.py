from django.urls import path
from document import views

app_name = 'document'

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('inbox/', views.InboxListView.as_view(), name='inbox'),
        ]
