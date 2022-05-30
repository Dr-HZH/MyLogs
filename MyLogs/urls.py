"""MyLogs URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

urlpatterns = [
    # 'admin/'代表127.0.0.1:8000/admin的路由地址，admin.site.urls指向内置Admin功能所定义的路由信息
    path('admin/', admin.site.urls),
    # '' 代表路由地址为’\‘，即127.0.0.1:8000，一般是网站首页，路由函数include是将该路由信息分发给plogs的urls.py处理。
    path('', include('plogs.urls')),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media')
]
