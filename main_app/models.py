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
  
class Reservation(models.Model):
    user = models.CharField(max_length=100)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} is staying at {self.resort.name} from {self.check_in} to {self.check_out}"
    
class Review(models.Model):
    user = models.CharField(max_length=100)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} rated {self.resort.name} {self.rating} stars"