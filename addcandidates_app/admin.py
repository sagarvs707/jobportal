from django.contrib import admin
# Register your models here.
from addcandidates_app.models import It_Jobs, Non_It_Jobs, Delivery_Boy

class Search_Candidate(admin.ModelAdmin):

    list_filter = ['valid']
    search_fields =['name', 'email',]
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(It_Jobs, Search_Candidate)
admin.site.register(Non_It_Jobs, Search_Candidate)
# admin.site.register(Delivery_Boy, Search_Candidate)