from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300, blank=True)
    email = models.EmailField()
    phone = models.CharField( max_length=300)
    message = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'