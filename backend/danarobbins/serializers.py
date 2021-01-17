from rest_framework import serializers
from .models import Gigs

class GigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gigs
        fields = ('id', 'venue', 'time', 'artist_name','ticket_link')
