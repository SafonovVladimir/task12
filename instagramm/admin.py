from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(PostTag)
