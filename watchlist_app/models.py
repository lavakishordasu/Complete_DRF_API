from django.db import models # type: ignore
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


# basic implementing models
# # Create your models here.
# class Movie(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name



# Updateing models with new fields
# adding relationships
# one to many   (3.22)
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name



class WatchList(models.Model):   #one-to-many relationship
    tittle = models.CharField(max_length=30)
    storyline = models.CharField(max_length=200)
    plateform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
    

# serializers relations(3.26)

class Review(models.Model):   #one-to-many relationship
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.watchlist.tittle + " -- " + str(self.rating)+"*" + " | " + str(self.review_user)



# 