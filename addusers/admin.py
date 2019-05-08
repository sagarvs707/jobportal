from django.contrib import admin
from .models import AddUsers

class Search_Candidate(admin.ModelAdmin):

    search_fields =['first_name', 'email',]
    ordering = ('first_name',)
    filter_horizontal = ()

admin.site.register(AddUsers, Search_Candidate)

