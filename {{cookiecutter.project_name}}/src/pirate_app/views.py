from django.http import JsonResponse
from .jokes import get_random_joke

def tell_joke(request):
    return JsonResponse({"joke": get_random_joke()})