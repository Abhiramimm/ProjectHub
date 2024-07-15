from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):

    title=models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    github_link=models.URLField(max_length=200)

    image=models.ImageField(upload_to="project_images",null=True,blank=True,default="project_images/default.jpg")

    project_preview=models.FileField(upload_to="project_videos",null=True,blank=True)


    def __str__(self):

        return self.title

class Wishlist(models.Model):

    project_object=models.ForeignKey(Project,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


