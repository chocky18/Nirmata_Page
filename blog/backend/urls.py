from django.urls import path

from .api import authors, posts

urlpatterns = [
    path('authors', authors.get),
    path('authors/<int:id>', authors.get_by_id),
    path('posts', posts.get),
    path('posts/<int:id>', posts.get_by_slug),
]
