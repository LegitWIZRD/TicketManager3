from django.db import models

# Create your models here.


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    entry_1 = models.CharField(max_length=50)
    entry_2 = models.CharField(max_length=20)
    entry_3 = models.CharField(max_length=40)
    entry_4 = models.CharField(max_length=10)
    entry_5 = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.created_at} {self.entry_1} {self.entry_2} {self.entry_3} {self.entry_4} {self.entry_5}"
