from django.db import models

class EmailModel(models.Model):
    email=models.TextField()

    def __str__(self):
        return self.email
    