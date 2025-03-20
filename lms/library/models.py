from django.db import models

from django.core.validators import MinLengthValidator

from authors.models import Author


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    number_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"