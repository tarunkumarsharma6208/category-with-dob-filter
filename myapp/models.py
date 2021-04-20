from django.db import models
from django.urls import reverse


class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('article_by_category', args=[self.slug,])


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


