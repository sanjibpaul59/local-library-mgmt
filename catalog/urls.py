from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r"index", views.HomeView, basename="home")

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("books/", views.BookList.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetail.as_view(), name="book-detail"),
    path("authors/", views.AuthorList.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetail.as_view(), name="author-detail"),
    path("language/<int:pk>", views.LanguageDetail.as_view(), name="language-detail"),
    path("genre/<int:pk>", views.GenreDetail.as_view(), name="genre-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
