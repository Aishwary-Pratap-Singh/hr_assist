from django.db import models

class DocumentText(models.Model):
    DOC_TYPE_CHOICES = [
        ('jd', 'Job Description'),
        ('resume', 'Resume'),
    ]
    file_name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=10, choices=DOC_TYPE_CHOICES)
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name} ({self.doc_type})"

# Create your models here.
