from django.http import JsonResponse

from ..models import Author


def get(request):
    authors = Author.get_list()
    return JsonResponse({'data': authors})


def get_by_id(request, id):
    return JsonResponse({'data': Author.get_by_id(id)})
