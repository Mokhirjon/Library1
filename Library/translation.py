from modeltranslation.translation import translation, FieldTranslation
from .models import Books,Library,Author


class LibraryTrans(FieldTranslation):
    fields = ('name', 'fname', 'text')


class ModelWithTranslator(LibraryTrans):
     fields = ('name', 'fname', 'text')


translation.register(Library, LibraryTrans)