from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=192)

    def __str__(self):
        return self.full_name
