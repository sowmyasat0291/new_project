from django.db import models

# Define your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()  # Use TextField for larger text fields

    def __str__(self):
        return self.name
