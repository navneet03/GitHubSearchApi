from django.contrib import admin
from django.db.models import Count

from GitHubUserApp.models import *

# Register your models here.

class AdminGitHubUser(admin.ModelAdmin):

    list_display = ['user_id', 'image_tag', 'user_name', 'email', 'created_date', 'added_date', 'location',
                    'no_of_followers', 'no_of_repos']
    readonly_fields = ['image_tag']
    ordering = ['added_date']
    list_filter = ['location', 'no_of_followers', 'no_of_repos', 'created_date']
    search_fields = ['added_date', 'email']

admin.site.register(GitHubUserDetails, AdminGitHubUser)
