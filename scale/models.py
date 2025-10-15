from django.db import models

# Create your models here.
class SiteActivity(models.Model):
    EVENT_TYPES = [
        ('page_view', 'Page View'),
        ('click', 'Click'),
        ('form_submit', 'Form Submit'),
        ('login', 'Login'),
    ]

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    page_url = models.URLField()
    user_ip = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} at {self.page_url}"