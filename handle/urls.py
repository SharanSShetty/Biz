from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('alogin/', TemplateView.as_view(template_name='control/alogin.html'), name='admin_login'),
    path('ahome/', TemplateView.as_view(template_name='control/ahome.html'), name='admin_home'),
    path('approve-businesses', TemplateView.as_view(template_name='control/approve_businesses.html'), name='approve_businesses'),
    path('manage_business/', TemplateView.as_view(template_name='control/manage_business.html'), name='manage_business'),
    path('manage/', TemplateView.as_view(template_name='control/manage_users.html'), name='manage_users'),
]
