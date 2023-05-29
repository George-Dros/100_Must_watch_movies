import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
titles_data_list = soup.find_all("h3")

titles_list = []

for title_data in titles_data_list:
    title = title_data.getText()
    titles_list.append(title)

titles_list.reverse()

with open("100 Movies.txt", "w", encoding="utf-8") as file:
    for movie in titles_list:
        file.write(movie+"\n")
