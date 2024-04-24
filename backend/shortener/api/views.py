from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from shortener.models import URL
from shortener.api.serializers import URLSerializer, URLHashedReturnSerializer

@api_view(["GET", "POST"])
def index(request):
    if request.method == 'GET':
        urls = URL.objects.all()
        serializer = URLHashedReturnSerializer(urls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.save()
            serializer_ret = URLHashedReturnSerializer(url)
            
            return Response(serializer_ret.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)