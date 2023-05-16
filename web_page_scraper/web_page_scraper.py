import os
import requests
from bs4 import BeautifulSoup


def parse_nature_website(num_pages, article_type):
    # Создаем отдельную директорию для страниц и файлов
    pages_dir = "Pages"
    os.makedirs(pages_dir, exist_ok=True)

    for i in range(1, num_pages + 1):
        # Создаем директорию с именем "Page_i" внутри директории "Pages"
        page_dir = os.path.join(pages_dir, f"Page_{i}")
        os.makedirs(page_dir, exist_ok=True)

        # Получаем содержимое страницы
        url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i}"
        r = requests.get(url)

        # Разбираем содержимое страницы
        soup = BeautifulSoup(r.content, "html.parser")

        # Находим все статьи на странице и фильтруем их по типу статьи
        articles = soup.find_all("article")
        articles = [a for a in articles if a.find("span", {"class": "c-meta__type"}).text.strip() == article_type]

        # Записываем каждую статью в соответствующий файл *.txt
        for j, article in enumerate(articles):
            title = article.find("a", {"data-track-action": "view article"}).text.strip()
            filename = f"{j+1}. {title}.txt"
            filepath = os.path.join(page_dir, filename)

            # Получаем содержимое статьи и записываем его в файл
            article_url = f"https://www.nature.com{article.find('a', {'data-track-action': 'view article'})['href']}"
            article_r = requests.get(article_url)
            article_soup = BeautifulSoup(article_r.content, "html.parser")
            article_body = article_soup.find("div", {"class": "c-article-body"})
            article_text = article_body.text.strip() if article_body is not None else ""

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(article_text)


        print(f"Saved all articles on page {i}.")
        # Создаем папку для текущей страницы и перемещаем в нее все файлы
        page_dir_sorted = f"{article_type}_{page_dir}"
        os.makedirs(page_dir_sorted, exist_ok=True)
        for file in os.listdir(page_dir):
            file_path = os.path.join(page_dir, file)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    file_text = f.read()
                folder_name = "Other"
                if "News.NATURE BRIEFING" in file_text:
                    folder_name = "Nature Briefing"
                elif "Research Highlights" in file_text:
                    folder_name = "Research Highlights"
                elif "Editorial" in file_text:
                    folder_name = "Editorials"
                elif "News Feature" in file_text:
                    folder_name = "News Features"
                folder_path = os.path.join(page_dir_sorted, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                new_file_path = os.path.join(folder_path, file)
                os.rename(file_path, new_file_path)

    # Сортировка папок
    folders = os.listdir(pages_dir)

    # Сортировка по размеру
    folders.sort(key=lambda x: os.path.getsize(os.path.join(pages_dir, x)), reverse=True)
    print(f"Sorted folders by size: {folders}")

    # Сортировка по имени
    folders.sort()
    print(f"Sorted folders by name: {folders}")


num_pages = int(input("Enter the number of pages to scrape: "))
article_type = input("Enter the article type to scrape: ")
parse_nature_website(num_pages, article_type)

