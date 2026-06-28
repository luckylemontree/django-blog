from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)   

    profile_image = CloudinaryField('image', default='placeholder')
  
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written on {self.created_on}"

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)  
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default = False)

    def __str__(self):
        return f"Collaboration request from {self.name}"