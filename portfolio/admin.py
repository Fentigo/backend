from django.contrib import admin
from .models import Poet
from .models import SocialMedia
from .models import Bookings
from .models import Video
from .models import Image


class PoetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'contact_info')

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('site','url')

class BookingsAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'email',
    'message'
    )
class VideoAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'caption',
        'video_file' 
    )
class ImageAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'caption',
        'image_file' 
    )

    
admin.site.register(Poet, PoetAdmin)
admin.site.register(Bookings, BookingsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)

