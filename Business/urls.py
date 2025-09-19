from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='owner/login.html'), name='ologin'),
    path('register/', TemplateView.as_view(template_name='owner/register.html'), name='register'),
    path('home/', TemplateView.as_view(template_name='owner/home.html'), name='home'),
    path('addbusiness', TemplateView.as_view(template_name='owner/add_business.html'), name='addbusiness'),
    path('manage_business/', TemplateView.as_view(template_name='owner/manage_business.html'), name='manage_business'),
    path('business/<int:business_id>/visitors/', TemplateView.as_view(template_name='owner/visitedusers.html'), name='visited_users'),
    path('contact/', TemplateView.as_view(template_name='owner/contact.html'), name='contact_us'),
    path('success/', TemplateView.as_view(template_name='owner/success.html'), name='success_page'),
    path('forgot-password/', TemplateView.as_view(template_name='owner/forgot_password.html'), name='forgot_password'),
    path('reset-password/<str:token>/', TemplateView.as_view(template_name='owner/reset_password.html'), name='reset_password'),
    path('reviews/', TemplateView.as_view(template_name='owner/owner_reviews.html'), name='owner_reviews'),
    path('delete/<int:review_id>/', TemplateView.as_view(template_name='owner/confirm_delete.html'), name='delete_review'),
]
