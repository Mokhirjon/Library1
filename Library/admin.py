from django.contrib import admin
from .models import Books,Author,Library
from .forms import Librarylanguages
# Register your models here.
class Libraryadmin(admin.ModelAdmin):
    form = Librarylanguages
    list_display = ('id','book_name','author_name','Library_name')
    search_fields = ['book_name','author_name']
class BooksAdmin(admin.ModelAdmin):
    search_fields = ['name','id']
class AuthorsAdmin(admin.ModelAdmin):
    search_fields = ['author_name', 'id','author_books']


admin.site.register(Books,BooksAdmin)
admin.site.register(Author,AuthorsAdmin)
admin.site.register(Library,Libraryadmin)