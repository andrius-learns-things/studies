from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ItemSerializer
from .models import Item


@csrf_exempt
def item_list(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
