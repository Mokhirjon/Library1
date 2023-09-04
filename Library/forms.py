from django import forms
from .models import Library,Books,Author
class Librarylanguages(forms.ModelForm):

    Library_name_en = forms.CharField()
    Library_name_uz = forms.CharField(required=False)
    Library_name_ru = forms.CharField(required=False)

    book_name_en = forms.CharField()
    book_name_uz = forms.CharField(required=False)
    book_name_ru = forms.CharField(required=False)

    author_name_en = forms.CharField()
    author_name_uz = forms.CharField(required=False)
    author_name_ru = forms.CharField(required=False)

    bname_en = forms.CharField()
    bname_uz = forms.CharField(required=False)
    bname_ru = forms.CharField(required=False)

    Author_name_en = forms.CharField()
    Author_name_ru = forms.CharField(required=False)
    Author_name_uz = forms.CharField(required=False)



    Author_books_en = forms.CharField()
    Author_books_uz = forms.CharField(required=False)
    Author_books_ru = forms.CharField(required=False)

    model = Library,Books,Author
    exclude = ['Library_name', 'bname', 'author_name','Author_name','Author_books','book_name']