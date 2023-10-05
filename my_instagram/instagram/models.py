from django.db import models

# Create your models here.

class mypost(models.Model):
    create_at= models.DateTimeField()
    image= models.ImageField(upload_to="instagram/images")
    title= models.CharField(max_length=200)
    caption= models.TextField()
    