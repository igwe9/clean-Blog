from django.contrib import admin
from POST.models import Author, post, picture,Entry,Blog

# Register your models here.
admin.site.register(Author)
admin.site.register(post)
admin.site.register(picture)
admin.site.register(Entry)
admin.site.register(Blog)
