from rest_framework import serializers
from .models import BookData

class BookSerializer(serializers.ModelSerializer):
    Image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=BookData
        fields = ['id', 'Name', 'Category', 'Description', 'Rating', 'Image']