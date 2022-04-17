from django.db import models


class File(models.Model):
    STATUS_CHOICES = [
        ('ENC', 'Encrypted'),
        ('DEC', 'Decrypted'),
        ('DEL', 'Deleted')
    ]
    
    filename = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Add owner field
