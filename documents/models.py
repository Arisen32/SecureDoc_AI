import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Document(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Processing'),
        ('PROCESSING', 'Processing RAG'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    file_size = models.IntegerField(help_text="Tamaño en bytes")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Integración con Azure AI Search
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    azure_index_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.owner.username}"

    