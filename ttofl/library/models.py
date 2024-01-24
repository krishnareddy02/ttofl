from django.db import models

# Create your models here.


class books_data1(models.Model):
    name=models.CharField(max_length=1000)
    pages=models.IntegerField()
    author_name=models.CharField(max_length=100)
    genre=models.CharField(max_length=100,default="unknown book")
    email=models.EmailField(default="null@gmail.com")
    # book_image=models.ImageField(upload_to='media/',null=True,blank=True)

class register_details1(models.Model):
    unique_user_code=models.CharField(max_length=1000,default="null")
    is_admin=models.IntegerField(default=0)
    email=models.EmailField()
    password=models.CharField(max_length=100)

class books_1(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100,default="null")
    user_id=models.CharField(max_length=100)
    name=models.CharField(max_length=1000)
    phone=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='media/',null=True,blank=True)

