from django.contrib import admin
# Register your models here.
from addcandidates_app.models import AddCandidate

class Search_Candidate(admin.ModelAdmin):

    list_filter = ['valid']
    search_fields =['name', 'email',]
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(AddCandidate, Search_Candidate)