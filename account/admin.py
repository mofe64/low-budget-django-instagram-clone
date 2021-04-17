from django.contrib import admin
from .models import Author


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')


admin.site.register(Author, AuthorAdmin)
