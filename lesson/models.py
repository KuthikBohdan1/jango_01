from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    bio =  models.TextField()
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")



    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course")


class Course(models.Model):
    title = models.CharField(max_length=200)