from django.urls import path
from document import views

app_name = 'document'

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('inbox/', views.InboxListView.as_view(), name='inbox'),
        path('inbox/accept/', views.InboxCreateView.as_view(), name='accept'),
        path('inbox/<int:pk>/', views.InboxDetailView.as_view(), name='inbox-detail'),
        path('inbox/<int:pk>/update/', views.InboxUpdateView.as_view(), name='inbox-update'),

        path('inbox/to-me/', views.to_me, name='to-me'),
        path('inbox/to-sector/', views.to_sector, name='to-sector'),

        path('outbox/', views.OutboxListView.as_view(), name='outbox'),
        path('outbox/send/', views.OutboxCreateView.as_view(), name='send'),
        ]
