from django.db import models
from login.models import User, UserManager

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  ingredients = models.TextField(default=None)
  instructions = models.CharField(max_length=255, default=None)
  servings = models.CharField(max_length=255, default=None)
  prep_time = models.CharField(max_length=255, default=None)
  cook_time = models.CharField(max_length=255, default=None)
  uploader = models.ForeignKey(User, related_name="upload_recipes",on_delete=models.CASCADE)
  users_who_like = models.ManyToManyField(User, related_name='liked_recipes')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)