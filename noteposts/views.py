from django.shortcuts import render
from .models import NotePosts
from rest_framework import viewsets
from .serializers import NoteSerializer

# Create your views here.


class NotePostsViewset(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    queryset=NotePosts.objects.all()