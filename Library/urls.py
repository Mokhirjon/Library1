from django.urls import path
from .views import (LibraryCreateApiview,LibraryDeleteApiview,LibraryListApiview,
                    LibraryDetelesApiview,LibraryUpdatesApiview)
urlpatterns=[
    path('all/',LibraryListApiview.as_view()),
    path('update/<int:Library_id>/',LibraryUpdatesApiview.as_view()),
    path('create/<int:Library_id>/',LibraryCreateApiview.as_view()),
    path('delete/<int:Library_id>/',LibraryDeleteApiview.as_view()),
    path('deteles/<int:Library_id>/',LibraryDetelesApiview.as_view()),
]