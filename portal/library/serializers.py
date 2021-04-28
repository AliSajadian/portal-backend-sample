from rest_framework import serializers
from library.models import Library_Book_Type, Library_Book_Publisher, Library_Book_Author, Library_Book, Library_Loaned_Book



class Library_Book_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Book_Type
        fields = '__all__'

class Library_Book_PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Book_Publisher
        fields = '__all__'

class Library_Book_AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Book_Author
        fields = '__all__'

class Library_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Book
        fields = '__all__'

class Library_Loaned_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_Loaned_Book
        fields = '__all__'

