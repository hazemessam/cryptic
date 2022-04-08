from django.db import models


class File(models.Model):
    filename = models.CharField(max_length=100, unique=True)
    STATUS_CHOICES = [
        ('ENC', 'encrypted'),
        ('DEC', 'decrypted'),
        ('DEL', 'deleted')
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    updated_at = models.DateTimeField(auto_now=True)

    # TODO
    # Add owner_id field
