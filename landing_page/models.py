from django.db import models

# Create your models here.
class Visitor(models.Model):
    email = models.EmailField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date = self.timestamp.date()
        return "{}     ({})".format(self.email, self.timestamp)
