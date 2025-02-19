from django.db import models

from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

class Resort(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  price = models.IntegerField()
  image = models.CharField(max_length=1000)
  description = models.TextField()
  favorite = models.BooleanField(default=False)
  favorite_by = models.ManyToManyField(User, related_name='favorite_resorts')
  
  def __str__(self):
    return self.name
  
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} is staying at {self.resort.name} from {self.check_in} to {self.check_out}"
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} rated {self.resort.name} {self.rating} stars"
    
class Meta:
    ordering = ['-date']