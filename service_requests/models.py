from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceRequest(models.Model):
    TYPE_CHOICES = [
        ('Repair', 'Repair'),
        ('Installation', 'Installation'),
        ('Inquiry', 'Inquiry'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='pending',
        )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    details = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.customer.username}"
