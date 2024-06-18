from django.db import models

class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
