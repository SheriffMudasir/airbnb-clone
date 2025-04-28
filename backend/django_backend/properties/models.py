import uuid
from django.conf import settings
from django.db import models

from useraccount.models import User

class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    max_guests = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    #favourited
    image = models.ImageField(upload_to='uploads/properties/')
    landlord = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Properties' 
        ordering = ['-created_at']
    
    # Existing code ...
    def image_url(self):
        if self.image:
            return f"{settings.WEBSITE_URL}{self.image.url}"

    