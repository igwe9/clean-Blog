from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



# Custom admin name
admin.site.site_header = 'Eminent Blog' #login page
admin.site.index_title = 'Eminent Blog Administration '
admin.site.site_title = 'Site'
admin.site.site_index = 'Eminent Adminstrator'

name = 'Eminent'
urlpatterns = [
    path('', include('POST.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
