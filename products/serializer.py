from rest_framework import serializers

from .models import Estate, File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file')


class EstateSerializer(serializers.HyperlinkedModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = Estate
        fields = (
        'url', 'id', 'title', 'city', 'address', 'meterage', 'parking', 'storeroom', 'description', 'price', 'files')
