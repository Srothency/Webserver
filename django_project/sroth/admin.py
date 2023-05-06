from django.contrib import admin
from .models import Post
from .models import MyModel
from .models import App

admin.site.register(Post)
admin.site.register(MyModel)
admin.site.register(App)

