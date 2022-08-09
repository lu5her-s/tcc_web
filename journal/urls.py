from django.urls import path
from journal import views

app_name = 'journal'

urlpatterns = [
    path('', views.JournalListView.as_view(), name="list"),
    path('create/', views.JournalCreateView.as_view(), name="create"),
    path('<int:pk>/', views.JournalDetailView.as_view(), name="detail"),
]
