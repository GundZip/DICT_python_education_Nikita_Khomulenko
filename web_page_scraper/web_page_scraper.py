import requests
from bs4 import BeautifulSoup
import string

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

articles = soup.find_all("article")

for article in articles:
    article_type = article.find("span", {"data-test": "article.type"}).text.strip()

    if article_type == "News":
        article_link = article.find("a", {"data-track-action": "view article"})
        article_title = article_link.text.strip() if article_link else "untitled"
        article_title = article_title.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")
        article_body = article.find("div", {"class": "c-article-body"})
        article_text = article_body.text.strip() if article_body else "no content"
        article_text = article_text.replace("\n", "").replace("\r", "").replace("\t", "").replace("\xa0", " ")
        article_title = article_title.replace(" ", "_")
        with open(f"{article_title}.txt", "w", encoding="utf-8") as file:
            file.write(article_text)
        print(f"{article_title}.txt saved successfully.")