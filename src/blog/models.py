from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()



# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100) # le champ max_length est obligatoire pour ce field.
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField(default="")
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    category = models.ManyToManyField(Category)
    
    def save_slug(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)


