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
    # Recupera o documento PDF pelo seu ID
    try:
        pdf = PDFDocument.objects.get(id=pdf_id)
    except PDFDocument.DoesNotExist:
        return HttpResponse("PDF not found", status=404)

    if request.method == 'POST':
        # Processa os dados submetidos pelo formulário
        name = request.POST.get('name')
        option1 = request.POST.get('checkbox1') == 'on'
        option2 = request.POST.get('checkbox2') == 'on'

        # Exemplo: salvando os dados em algum lugar
        # Aqui você deve implementar a lógica necessária para processar os dados do formulário
        # Por exemplo, salvar em banco de dados ou fazer alguma outra operação

        # Redireciona para alguma página após o processamento dos dados
        return redirect('home')  # Redireciona para a página inicial, ajuste conforme necessário
    else:
        # Caso GET, apenas renderiza o template com o formulário
        return render(request, 'app/pdf_and_form.html', {'pdf': pdf})
    

def submit_details(request, pdf_id):
    if request.method == 'POST':
        # Processar os dados do formulário aqui
        return redirect('home')  # Redirecionar para a página inicial após o processamento
    else:
        # Tratar o caso de método GET, se necessário
        return HttpResponse("Method not allowed", status=405)
    
