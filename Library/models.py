from django.db import models

# Create your models here.
class Library(models.Model):
    Library_name=models.CharField(max_length=35,default='')
    book_name=models.CharField(max_length=35,default='')
    author_name=models.CharField(max_length=25,default='')

    def __str__(self):
        return self.Library_name
class Books(models.Model):
    name=models.CharField(max_length=35,default='')
    book_price = models.IntegerField()
    book_year = models.DateField()
    Library_id=models.ForeignKey(Library,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
class Author(models.Model):
    Author_name = models.CharField(max_length=25,default='')
    Author_bday = models.DateField()
    Author_books = models.CharField(max_length=55,default='')
    Library_id = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Author_name
