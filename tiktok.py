import requests
import json
from keys import API_KEY

class Tiktok:

    def get_authors(self):
        authors_list = []

        url = "https://tiktok-download-video1.p.rapidapi.com/feedList"

        querystring = {"region":"US","count":"10"}

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        for video in json_data["data"]:
            authors_list.append({'unique_id': f'{video["author"]["unique_id"]}', 'user_id': f'{video["author"]["id"]}', 'nickname': f'{video["author"]["nickname"]}' })

        return authors_list


    def get_follower_count(self,unique_id, user_id):
        url = "https://tiktok-download-video1.p.rapidapi.com/userInfo"

        querystring = {"unique_id":f"@{unique_id}","user_id":user_id}

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        return int(json_data["data"]["stats"]["followerCount"])


    def get_followers(self, user_id):
        url = "https://tiktok-download-video1.p.rapidapi.com/userFollowerList"

        querystring = {"user_id": user_id,"count":"50","time":"0"}

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        return json_data["data"]["followers"]
    
    def run_scan(self, min_followers: int, max_followers: int):
        qualified_authors = []
        with open('followers.json', 'r') as json_file:
            data = json.load(json_file)
        
        for follower in data["data"]["followers"]:
            qualified_authors.append(follower)
        # desired_authors = 3
        # first_authors = self.get_authors()

        # while len(qualified_authors) < desired_authors:

        #     for author in first_authors:
        #         # check how many followers author has
        #         followers_count = self.get_follower_count(author["unique_id"], author["user_id"])
        #         if followers_count > min_followers and followers_count < max_followers:
        #             author["follower_count"] = followers_count
        #             qualified_authors.append(author)
        #             if len(qualified_authors) == desired_authors:
        #                 break

        #         # get a list of authors followers
        #         author_followers = self.get_followers(author["user_id"])

        #         # check follower number for each followers
        #         for author_follower in author_followers:
        #             followers_count = author_follower["follower_count"]
        #             if followers_count > min_followers and followers_count < max_followers:
        #                 author_follower["follower_count"] = followers_count
        #                 qualified_authors.append(author_follower)
        #                 if len(qualified_authors) == desired_authors:
        #                     break
        
        return qualified_authors


