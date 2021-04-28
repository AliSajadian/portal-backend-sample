from rest_framework import viewsets, permissions
from library.models import Library_Book_Type, Library_Book_Publisher, Library_Book_Author, Library_Book, Library_Loaned_Book
from .serializers import Library_Book_TypeSerializer, Library_Book_PublisherSerializer, Library_Book_AuthorSerializer, Library_BookSerializer, Library_Loaned_BookSerializer
from rest_framework.response import Response
from django.db.models import F



class Library_Book_TypeViewSet(viewsets.ModelViewSet):
    queryset = Library_Book_Type.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Library_Book_TypeSerializer


class Library_Book_PublisherViewSet(viewsets.ModelViewSet):
    queryset = Library_Book_Publisher.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Library_Book_PublisherSerializer


class Library_Book_AuthorViewSet(viewsets.ModelViewSet):
    queryset = Library_Book_Author.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Library_Book_AuthorSerializer

class Library_BookViewSet(viewsets.ModelViewSet):
    queryset = Library_Book.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Library_BookSerializer


class Library_Loaned_BookViewSet(viewsets.ModelViewSet):
    queryset = Library_Loaned_Book.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ] 

    serializer_class = Library_Loaned_BookSerializer