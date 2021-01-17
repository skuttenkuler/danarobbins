from rest_framework import serializers
from .models import Gig

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ('id', 'venue', 'time', 'artist_name','ticket_link')
