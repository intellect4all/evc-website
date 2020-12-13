from django.db import close_old_connections, models
from django.db.models.fields import DateTimeField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=155)
    value = models.IntegerField()
    area = models.IntegerField()
    date_added = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']