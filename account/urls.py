from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile-update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('password/', views.PasswordView.as_view(), name='password'),
    
    path('members/', views.MemberListView.as_view(), name='members'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member'),

    path('line-token/', views.LineTokenListView.as_view(), name='line-token'),
    path('line-token-create/', views.LineTokenCreateView.as_view(), name='line-token-create'),
    path('line-token-update/<int:pk>', views.LineTokenUpdateView.as_view(), name='line-token-update'),
]