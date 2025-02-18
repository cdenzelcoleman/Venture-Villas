from django.db import models

class Resort(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  price = models.IntegerField()
  image = models.CharField(max_length=1000)
  description = models.TextField()
  favorite = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name
