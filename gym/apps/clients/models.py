from django.db import models

class Client(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('passport', 'Passport'),
        ('driver_license', 'Driver License'),
        ('national_id', 'National ID'),
    ]

    name = models.CharField(max_length=100, verbose_name="Full Name", blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    document_number = models.CharField(max_length=20)
    document_type = models.CharField(max_length=17, choices=DOCUMENT_TYPE_CHOICES)

    def __str__(self):
        return self.name
