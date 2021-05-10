import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")  # here we are downloadin the questions of  stackoverflow
soup = BeautifulSoup(response.text, "html.parser")  # response.text will return the html content of the web page.

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())