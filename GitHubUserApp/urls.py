from django.conf.urls import url
from django.contrib import admin
from GitHubUserApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^save_github_user_details/', views.SaveUserDetails.as_view()),
]