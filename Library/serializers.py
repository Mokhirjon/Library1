from rest_framework import serializers

class LibrarySerializers(serializers.Serializer):
    Library_name = serializers.CharField()
    book_name = serializers.CharField()
    author_name = serializers.CharField()

    def __str__(self):
        return self.Library_name


class BookSerializers(serializers.Serializer):
    bname = serializers.CharField()
    book_price = serializers.IntegerField()
    book_year = serializers.DateField()

    def __str__(self):
        return self.name


class AuthorSerializers(serializers.Serializer):
    Author_name = serializers.CharField()
    Author_bday = serializers.DateField()
    Author_books = serializers.CharField()

