# service_requests/models.py

from django.db import models
from django.contrib.auth.models import User
class ServiceRequest(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    #resolved_at = models.DateTimeField(null=True, blank=True)
    #status = models.CharField(max_length=50, default='Pending')
    class Meta:
        app_label = 'service_requests'


class Customer(User):
    name = models.CharField(max_length=255)
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=255)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return self.name

