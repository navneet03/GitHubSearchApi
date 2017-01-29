from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import logging

from db_service import DbService
from git_hub_api_service import GitHubApiService

db_service = DbService()
git_api_service = GitHubApiService()
log = logging.getLogger('GitHuUserApp')


class SaveUserDetails(APIView):
    def post(self, request):
        try:
            search_list = git_api_service.search_git_hub_user(request.data)
            if search_list == "failure":
                return Response({"status": 205, "data": "Something went wrong In GitHubSearchApi"})
            db_service.save_github_user_details(search_list)
            return Response({"data": "success", "statusCode": 200})
        except Exception, e:
            log.debug(str(e) + " IN  SaveUserDetails GetRestApi")
            return Response({"data": "failure", "statusCode": 404})
