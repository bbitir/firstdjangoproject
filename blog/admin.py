from django.contrib import admin
from .models import Post

admin.site.register(Post) # modelimizi admin sayfasında görünür yapmak için modeli belirtmek gerekir.
# Register your models here.
