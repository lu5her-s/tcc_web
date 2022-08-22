"""app_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# for test template
from django.views.generic import TemplateView
from account.views import HomeView

urlpatterns = [
    # admin external app
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    
    path('admin/', admin.site.urls),
    # for test template
    path('', HomeView.as_view(), name='home'),
    
    # for manage user account
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),

    path('announce/', include('announce.urls', namespace='announce')),
    path('asset/', include('asset.urls', namespace='asset')),
    path('journal/', include('journal.urls', namespace='journal')),
    path('assign/', include('assign.urls', namespace='assign')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
