from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default="", null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default="", null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=500, null=True, blank=True, default="")
    excerpt = models.CharField(max_length=256, null=True, blank=True, default="")
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    cats = models.ManyToManyField(Category, default='Uncategorized')
    tags = models.ManyToManyField(Tag, default="")
    image = models.ImageField(null=True)
    status = models.CharField(max_length=100, choices=STATUS, default="")

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField(max_length=30)
    subject = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    allowed = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default="", related_name="comments")

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.name

# Create your models here.
