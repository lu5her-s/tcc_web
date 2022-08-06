from django.urls import path

from asset import views

app_name = 'asset'
urlpatterns = [
    path('', views.AssetListView.as_view(), name='list'),
    path('<int:pk>/', views.AssetDetailView.as_view(), name='detail'),
    path('create/', views.AssetCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.AssetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AssetDeleteView.as_view(), name='delete'),

]
