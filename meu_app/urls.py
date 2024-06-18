from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('', views.pdf_list, name='pdf_list'),
    path('view/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
    path('pdf/<int:pdf_id>/', views.pdf_and_form, name='pdf_and_form'),
    path('submit/<int:pdf_id>/', views.submit_details, name='submit_details'),
]