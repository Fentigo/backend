from rest_framework import serializers
from .models import Poet
from .models import SocialMedia
from .models import Bookings
from .models import Video
from .models import Image

#serializers convert the model instances to JSON for the frontend to work with the data

class PoetSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Poet
        fields = ('first_name', 'last_name', 'dob', 'contact_info')
    
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields =('site','url')

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields  = ('name','email','message')

class VideoSerializer(serializers.ModelSerializer):
    model = Video
    fields = ('title', 'caption', 'video_file')

class ImageSerializer(serializers.ModelSerializer):
    model = Image
    fields = ('title', 'caption', 'image_file')

