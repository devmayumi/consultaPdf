from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import PDFDocument
from .forms import PDFUploadForm
from django.views.decorators.csrf import csrf_exempt
import os

#funções que fazer upload e metodo que lista os pdf e que faz a visualização
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFUploadForm()
    return render(request, 'app/upload_pdf.html', {'form': form})

def pdf_list(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'app/pdf_list.html', {'pdfs': pdfs})

def view_pdf(request, pdf_id):
    pdf = PDFDocument.objects.get(id=pdf_id)
    file_path = os.path.join(settings.MEDIA_ROOT, pdf.pdf.name)
    with open(file_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='application/pdf')
    
def pdf_and_form(request, pdf_id):
    # Obtenha o objeto PDF a partir do ID
    pdf_document = get_object_or_404(PDFDocument, pk=pdf_id)
    
    # Renderize a página pdf_and_form.html e passe o PDFDocument como contexto
    return render(request, 'app/pdf_and_form.html', {'pdf_document': pdf_document})

@csrf_exempt
def submit_details(request, pdf_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        checkbox1 = request.POST.get('checkbox1') == 'on'
        checkbox2 = request.POST.get('checkbox2') == 'on'

        # Process the data (e.g., save to the database, send an email, etc.)
        # ...

        return HttpResponse(f"Name: {name}, Option 1: {checkbox1}, Option 2: {checkbox2}")
    else:
        return HttpResponse("Invalid request method.")
    
