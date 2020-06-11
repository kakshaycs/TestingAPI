from django.contrib import admin
from .models import User, Question, Answer, Reply, Tag

# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Reply)
admin.site.register(Tag)

