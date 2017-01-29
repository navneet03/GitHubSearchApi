from datetime import datetime, timedelta
import requests, re, calendar
import logging

log = logging.getLogger('GitHuUserApp')


class GitHubApiService(object):

    @staticmethod
    def search_git_hub_user(data):
        try:
            link = "https://api.github.com/search/users"
            resp = requests.get(link, params=data)
            search_res = resp.json()
            return search_res["items"]
        except Exception, e:
            log.debug(str(e) + " IN  GitHubApiService:search_git_hub_user")
            return "failure"

    @staticmethod
    def get_user_profile_info(url):
        try:
            resp = requests.get(url)
            search_res = resp.json()
            return search_res
        except Exception, e:
            log.debug(str(e) + " IN  GitHubApiService:search_git_hub_user")
            return "failure"
