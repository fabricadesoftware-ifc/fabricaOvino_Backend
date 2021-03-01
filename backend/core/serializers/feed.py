<<<<<<< HEAD
from rest_framework import serializers

from backend.core.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["id", "name", "description"]
=======
from rest_framework import serializers 
from backend.core.models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["id", "name", "description"]
>>>>>>> origin/Dev-Maria
