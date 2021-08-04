from django.db import models

# Create your models here.
class Article(models.Model):

    name = models.CharField(max_length=63)
    astral_name = models.CharField(max_length=63)

    description = models.TextField(max_length=127)
    astral_description = models.TextField(max_length=127)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=63, null=True)

    article = models.TextField(max_length=4095)

    creation_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)

    online = models.BooleanField(default=True)

    def get_categories_from(articles):

        categories = []

        for article in articles:
            if article.category not in categories:
                categories.append(article.category)

        return categories


class Category(models.Model):

    name = models.CharField(max_length=63, unique=True)
    description = models.CharField(max_length=127)
