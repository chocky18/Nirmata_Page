from django.http import JsonResponse

from ..models import Post


def get(request):
    posts = Post.get_list()
    return JsonResponse({'data': posts})


def get_by_slug(request, slug):
    return JsonResponse({'data': Post.get_by_slug(slug)})
