from django.db import models


class File(models.Model):
    class Status(models.TextChoices):
        ENCRYPTED = ('ENC', 'Encrypted')
        DECRYPTED = ('DEC', 'Decrypted')
        DELETED = ('DEL', 'Deleted')
    
    filename = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=3, choices=Status.choices,
                              default=Status.ENCRYPTED)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Add owner field
