"""DatabaseInterface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include

admin.site.site_title = "CMDB PORTAL"
admin.site.site_header = "CMDB PORTAL"
admin.site.index_title = ""
admin.site.site_url = None

urlpatterns = [
    path('', admin.site.urls),
    path('import/', include('Base.urls')),
    path('', include('django.contrib.auth.urls')),
]
