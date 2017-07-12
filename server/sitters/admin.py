from django.contrib import admin
from .models import Review, Sitter, Owner, Dog

# Register your models here.
admin.site.register(Review)
admin.site.register(Sitter)
admin.site.register(Owner)
admin.site.register(Dog)
