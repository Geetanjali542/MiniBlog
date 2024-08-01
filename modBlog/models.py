from django.db import models

# Create your models here.


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    title = models.CharField(max_length=30, blank=False)
    categories = models.CharField(max_length=30, blank=False)
    tag = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to ="media/images/")  #when images is defined it will automaticlly create the folder when the image will be uploaded from frontend
    content = models.TextField(max_length=2000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name
    
    