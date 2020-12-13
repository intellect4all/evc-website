from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

class Post(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)
    excerpt = models.CharField(max_length=256, null=True, blank=True, default="")
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    cats = models.ManyToManyField(Category, default='Uncategorized')
    tags = models.ManyToManyField(Tag, default="")
    image = models.ImageField()
    status = models.CharField(max_length=100, choices=STATUS, default="")

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField(max_length=30, null=True)
    subject = models.CharField(max_length=150, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    allowed = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default="", related_name="comments")

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.name

# Create your models here.
