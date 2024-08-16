import requests
from bs4 import BeautifulSoup

response  = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

print(questions.get("id", 0))