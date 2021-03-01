from rest_framework import viewsets
<<<<<<< HEAD

from backend.core.models import Feed
from backend.core.serializers import FeedSerializer


class FeedViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
=======
from backend.core.models import Feed
from backend.core.serializers import FeedSerializer

class FeedViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
>>>>>>> origin/Dev-Maria
