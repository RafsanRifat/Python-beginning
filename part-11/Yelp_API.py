# Api client id is an unique koy.
# Api key:  Ppi key is like a password to an Api


import requests
import config


url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
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
