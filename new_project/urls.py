"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
'''from ajax_select import urls as ajax_select_urls'''
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^social/', include('social.urls')),
	url(r'', include('social_auth.urls')),
   # url(r'^social/$', RedirectView.as_view(url='/social')),
    #url(r'^private/$', 'views.private'),
       # url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
