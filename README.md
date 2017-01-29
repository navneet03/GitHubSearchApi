# Using Github user search API store all search result in database.

##Problem Statement:

  So, Problem is related to Github API usage which you can find on https://developer.github.com/v3/

1. Create API for searching the Users. 

2. Go through the Documentation and have provision of filtering the user available in the Api params.

3. As any API call is made, store all user related info in a Django table. You can use any database of your choice.
   Table should have only unique users stored, if duplicate entry come, update the user.

4. Show all the stored users in Admin Panel, with image if available as thumbnail.

5. In Admin Panel users can be searched on the basis date of added, there email. Add Filters which you have added the 2 point.

6. Create a Report in Admin Panel of No of users added to the database in a day, week and month. Also, how many search API calls has been made in a day, week and month.

##Technology Used:

 **Backend:** Django

 **Database:** Postgresql

##Implementation Overview:
    
  * Design a django class model to store the user information. 
  * Create "SaveUserDetails" DRF Post Api, make a request with data search query (eg: {"q": "navneet03"})
  * Make a get request using user search git Api "https://api.github.com/search/users" with above parameter(req data).
  * In response get list of search user, now store all user info in database.
  * Register the model in django admin.
  
