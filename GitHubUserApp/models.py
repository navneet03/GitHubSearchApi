from __future__ import unicode_literals
from django.db import models


class GitHubUserDetails(models.Model):

    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(null=True, max_length=300)
    image_url = models.URLField(null=True, max_length=300)
    url = models.URLField(null=True, max_length=300)

    type = models.CharField(null=True, max_length=200)
    score = models.DecimalField(max_digits=15, decimal_places=4, default=0.0)

    no_of_repos = models.PositiveIntegerField(null=True, default=0)
    no_of_followers = models.PositiveIntegerField(null=True, default=0)
    email = models.CharField(null=True, max_length=200)
    location = models.CharField(null=True, max_length=300)
    created_date = models.DateField(null=True)

    added_date = models.DateField(null=True)

    # site_admin = models.BooleanField(default=False)
    # html_url = models.URLField(null=True, max_length=300)
    # followers_url = models.URLField(null=True, max_length=300)
    # following_url = models.URLField(null=True, max_length=300)
    # gists_url = models.URLField(null=True, max_length=300)
    # starred_url = models.URLField(null=True, max_length=300)
    # subscriptions_url = models.URLField(null=True, max_length=300)
    # organizations_url = models.URLField(null=True, max_length=300)
    # repos_url = models.URLField(null=True, max_length=300)
    # events_url = models.URLField(null=True, max_length=300)
    # received_events_url = models.URLField(null=True, max_length=300)

    def image_tag(self):
        return u'<img src="%s" width="30" height="30"/>' % self.image_url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
