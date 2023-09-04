from rest_framework import generics
from .models import Library,Author,Books
from .serializers import LibrarySerializers
# Create your views here.

class LibraryListApiview(generics.ListAPIView):
    queryset =Library.objects.all()
    serializer_class =LibrarySerializers

class LibraryDetelesApiview(generics.RetrieveAPIView):
    queryset =Library.objects.all()
    serializer_class =LibrarySerializers

class LibraryUpdatesApiview(generics.UpdateAPIView):
    queryset =Library.objects.all()
    serializer_class =LibrarySerializers

class LibraryCreateApiview(generics.CreateAPIView):
    queryset =Library.objects.all()
    serializer_class =LibrarySerializers

class LibraryDeleteApiview(generics.DestroyAPIView):
    queryset =Library.objects.all()
    serializer_class =LibrarySerializers