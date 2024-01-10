from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from .author import Author


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    modified_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        indexes = [models.Index(fields=['slug'])]
        ordering = ['-created_at']
        get_latest_by = 'created_at'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @classmethod
    def get_by_slug(cls, slug):
        return cls.objects.filter(slug=slug).values().first()

    @classmethod
    def get_list(cls):
        return list(cls.objects.values())
