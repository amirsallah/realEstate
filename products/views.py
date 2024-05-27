from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Estate, File
from .serializer import EstateSerializer


class EstateListView(APIView):
    def get(self, request):
        estate = Estate.objects.all()
        serializer = EstateSerializer(estate, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EstateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstateDetailView(APIView):
    def get_object(self, pk):
        try:
            return Estate.objects.get(pk=pk)
        except Estate.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        estate = self.get_object(pk)
        serializer = EstateSerializer(estate, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        estate = Estate.objects.get(pk=pk)
        estate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        estate = self.get_object(pk)
        serializer = EstateSerializer(estate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
