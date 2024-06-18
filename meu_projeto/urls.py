from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from meu_app import views  # Importe as views do seu aplicativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meu_app/', include('meu_app.urls')),
    path('pdf/<int:pdf_id>/', views.pdf_and_form, name='pdf_and_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
