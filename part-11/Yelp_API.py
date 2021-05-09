# Api client id is an unique koy.
# Api key:  Ppi key is like a password to an Api


import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "LFZOrwkWiUxtGc1pYl_Ob38_KdexcpvrLJLvYAOYN_gg9-yiu2yX4Q0ghBxw7FcIyb2NIdSaj9FBXjZ2_DP24ni7Ejy9CBVGZnnnD6p6pCAoK1-DuIMS8TYuEoaXYHYx"
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)  # eikhane requests er get method use kora hoiche.
                                                                      # ja ekti response object return kore, ei respomse
                                                                      # object ekta error code show korbe, karon amra ekhono
                                                                      # yelp k bolinai j k amra. ei jonne amaderke api key
                                                                      # provide korte hobe, r eita holo--> authentication
businesses = response.json()["businesses"]
print(businesses)
# for business in businesses:
#     print("Name: ", business["name"])
#     print("Website-link: ", business["url"])
#     print("Reviews : ",business["review_count"])

names = [business["name"] for business in businesses ]
print(names)
