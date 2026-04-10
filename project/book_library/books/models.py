from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Store(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True
    )
    published_date = models.DateField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='books')
    stores = models.ManyToManyField(Store, related_name='books')

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.book.title}: {self.rating}"
