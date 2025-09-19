from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', TemplateView.as_view(template_name='user/register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='user/login.html'), name='login'),
    path('dashboard/', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('logout/', TemplateView.as_view(template_name='user/login.html'), name='logout'),
    path('business/<int:business_id>/', TemplateView.as_view(template_name='user/business_detail.html'), name='business_detail'),
    path('saved/', TemplateView.as_view(template_name='user/saved_businesses.html'), name='saved_businesses'),
    path('contact/', TemplateView.as_view(template_name='user/contact.html'), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='user/sucess.html'), name='contact_success'),
]
