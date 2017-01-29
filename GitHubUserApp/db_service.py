from datetime import datetime
from GitHubUserApp.models import *
from git_hub_api_service import GitHubApiService

git_api_service = GitHubApiService()


class DbService(object):

    @staticmethod
    def save_github_user_details(user_data_list):
        for user_data in user_data_list:
            try:
                user_id = user_data["id"]
                model_obj = GitHubUserDetails.objects.filter(user_id=user_id).first()
                if not model_obj:
                    model_obj = GitHubUserDetails.objects.create(user_id=user_id)
                model_obj.type = user_data["type"]
                model_obj.user_name = user_data["login"]
                model_obj.image_url = user_data["avatar_url"]
                model_obj.score = user_data["score"]
                model_obj.url = user_data["url"]

                user_profile_info = git_api_service.get_user_profile_info(user_data["url"])

                if user_profile_info == "failure":
                    continue
                model_obj.email = user_profile_info["email"]
                model_obj.no_of_repos = user_profile_info["public_repos"]
                model_obj.no_of_followers = user_profile_info["followers"]
                model_obj.created_date = user_profile_info["created_at"].split('T')[0]
                model_obj.added_date = datetime.today().date()
                model_obj.location = user_profile_info["location"]
                model_obj.save()
            except:
                continue

