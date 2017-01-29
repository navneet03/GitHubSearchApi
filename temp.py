from __future__ import unicode_literals
from django.db import models


class GitHubUserDetails(models.Model):

    user_id = models.IntegerField(primary_key=True)
    user_login = models.CharField(null=True, max_length=300)
    image_url = models.URLField(null=True, max_length=300)
    url = models.URLField(null=True, max_length=300)
    html_url = models.URLField(null=True, max_length=300)
    followers_url = models.URLField(null=True, max_length=300)
    following_url = models.URLField(null=True, max_length=300)
    gists_url = models.URLField(null=True, max_length=300)
    starred_url = models.URLField(null=True, max_length=300)
    subscriptions_url = models.URLField(null=True, max_length=300)
    organizations_url = models.URLField(null=True, max_length=300)
    repos_url = models.URLField(null=True, max_length=300)
    events_url = models.URLField(null=True, max_length=300)
    received_events_url = models.URLField(null=True, max_length=300)
    type = models.CharField(null=True, max_length=200)
    site_admin = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=15, decimal_places=4, default=0.0)

    added_date = models.DateField(null=True)

    class Meta:
        db_table = 'gitapi\".\"github_user_details'

    def image_thumb(self):
        return u'<img src="%s" /> % < ' + self.image_url + ' >'
