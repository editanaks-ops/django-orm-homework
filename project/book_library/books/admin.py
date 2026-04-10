from django.contrib import admin
from .models import Author, Book

from django.contrib import admin
from .models import Author, Book, Genre, Publisher, Store, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'published_date')
    search_fields = ('title', 'author__name', 'publisher__name')
    list_filter = ('publisher', 'published_date', 'genres', 'stores')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created_at')
    search_fields = ('book__title', 'comment')
    list_filter = ('rating', 'created_at')
