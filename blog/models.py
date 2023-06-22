from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    post_content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True,
                            default="", null=False, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts")
    
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email_adress = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")