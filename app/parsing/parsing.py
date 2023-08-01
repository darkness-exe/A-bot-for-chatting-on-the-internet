from bs4 import BeautifulSoup
import random

with open("app/parsing/index1.html", encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
question1 = soup.find('div', class_='entry-content').find_all('li')

with open("app/parsing/index2 .html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
question2 = soup.find('div', class_='e599d42b92530cddc130').find_all_next('li')

questions = question1 + question2
