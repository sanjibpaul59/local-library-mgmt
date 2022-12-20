from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.get("/")

serializer_context = {"request": Request(request)}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class BookListSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField(source="author.get_full_name")
    author_url = serializers.HyperlinkedIdentityField(view_name="author-detail", format="html")

    class Meta:
        model = Book
        fields = ["title", "url", "author", "author_url"]


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ["id", "imprint", "status", "due_back"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(source="author.get_full_name")
    author_url = serializers.HyperlinkedIdentityField(view_name="author-detail", format="html")
    language = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    copies = serializers.SerializerMethodField("get_book_instances")

    def get_book_instances(self, obj):
        copies = BookInstance.objects.filter(book=obj)
        return BookInstanceSerializer(copies, many=True).data

    class Meta:
        model = Book
        fields = ["url", "title", "author", "author_url", "summary", "isbn", "language", "genre", "copies"]


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["url", "first_name", "last_name"]


class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.SerializerMethodField("books_written_by_author")

    # def books_written_by_author(self, author):
    #     queryset = Book.objects.filter(author=author)
    #     return BookSerializer(queryset, many=True, context={"request": serializer_context}).data

    class Meta:
        model = Author
        fields = [
            "url",
            "first_name",
            "last_name",
            "date_of_birth",
            "date_of_death",
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
