from rest_framework import viewsets
from django.conf import settings
import os
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest
from .serializers import BookingsSerializer,PoetSerializer,SocialMediaSerializer,VideoSerializer, ImageSerializer
#from django.core.files.utils import get_valid_filename
from django.utils.text import get_valid_filename
from .models import Image
from .models import Poet
from .models import SocialMedia
from .models import Bookings
from .models import Video
from .models import Image


# Create your views here.
class PoetView(viewsets.ModelViewSet):
    serializer_class = PoetSerializer
    queryset = Poet.objects.all()

class SocialMediaView(viewsets.ModelViewSet):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

class BookingsView(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    queryset = Bookings.objects.all()

class VideoView(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

def get_poet_description(request, poet_id):
    try:
        poet = Poet.objects.get(pk=poet_id)
        description = poet.description
        return JsonResponse({'description': description})
    except Poet.DoesNotExist:
        return JsonResponse({'error': 'Poet not found'}, status=404)
def get_social_media_id(request, social_media_id):
    try:
        socialmedia = SocialMedia.objects.get(pk=social_media_id)
        url = socialmedia.url
        return JsonResponse({'url': url})
    except SocialMedia.DoesNotExist:
        return JsonResponse({'error': 'URL not found'}, status=404)
def get_image_file(request, image_id):
    try:
        image = Image.objects.get(pk=image_id)
        image_file_path = image.image_file.path
        # Assuming your images are stored in a directory named 'images'
        relative_path = os.path.relpath(image_file_path, settings.MEDIA_ROOT)
        # Construct the URL using the relative path
        image_url = f'../media/{relative_path}'
        return JsonResponse({'image_file': image_url})
    except Image.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        sanitized_filename = get_valid_filename(uploaded_file.name)
        #then we save the uploaded file to the relevant directory
        new_image = Image(image_file=uploaded_file) #i'm using the image model i created before. 
        new_image.save()
        return HttpResponse('File uploaded successfully')
    else:
        return HttpResponseBadRequest('No file provided or invalid request method')
def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        uploaded_file = request.FILES['video']
        sanitized_filename = get_valid_filename(uploaded_file.name)
        #then we save the uploaded file to the relevant directory
        new_video = Video(image_file=uploaded_file) #i'm using the Video model i created before. 
        new_video.save()
        return HttpResponse('File uploaded successfully')
    else:
        return HttpResponseBadRequest('No file provided or invalid request method')



