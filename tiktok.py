import requests
import json

class Tiktok:

    def get_authors(self):
        authors_list = []

        url = "https://tiktok-download-video1.p.rapidapi.com/feedList"

        querystring = {"region":"US","count":"10"}

        headers = {
            "X-RapidAPI-Key": "4ebb607162msh77a6d3c4a9f3b1dp16ead9jsn3d3abff5996f",
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        for video in json_data["data"]:
            authors_list.append({f'{video["author"]["unique_id"]}': f'{video["author"]["id"]}'})

        return authors_list


    def get_follower_count(self,unique_id, user_id):
        url = "https://tiktok-download-video1.p.rapidapi.com/userInfo"

        querystring = {"unique_id":f"@{unique_id}","user_id":user_id}

        headers = {
            "X-RapidAPI-Key": "4ebb607162msh77a6d3c4a9f3b1dp16ead9jsn3d3abff5996f",
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        return json_data["data"]["stats"]["followerCount"]


    def get_followers(self, user_id):
        url = "https://tiktok-download-video1.p.rapidapi.com/userFollowerList"

        querystring = {"user_id": user_id,"count":"50","time":"0"}

        headers = {
            "X-RapidAPI-Key": "4ebb607162msh77a6d3c4a9f3b1dp16ead9jsn3d3abff5996f",
            "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()

        return json_data["data"]["followers"]