from django.db import models

# Create your models here.


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ticket_number = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=40)
    description = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.created_at} {self.ticket_number} {self.contact_name} {self.contact_email} {self.description} {self.notes}"


