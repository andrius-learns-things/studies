from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ItemSerializer
from .models import Item


@csrf_exempt
def item_list(request):
    if request.method == "GET":
        return _get_all()

    if request.method == "POST":
        item = Item(name="New item")
        item.save()
        return _get_all()


def _get_all():
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)
