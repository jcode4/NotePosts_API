from .models import NotePosts
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotePosts
        fields='__all__'