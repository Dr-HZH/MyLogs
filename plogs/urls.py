from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.getIndex),
    path('Home', views.getIndex),
    path('Logs', views.getLogs),
    path('detail/plog/<int:plog_id>', views.getPlog),
    path('detail/Avatar/<int:Avatar_id>', views.getAvatar),
]
