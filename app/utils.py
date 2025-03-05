import requests
import os

API_KEY = ''

def get_google_books_info(query):
    """
    Function to search for book in the API
    """
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}'
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        if "items" in data and len(data["items"]) > 0:
            book = data["items"][0]["volumeInfo"]

            return {
                "title": book.get("title", "Título desconhecido"),
                "author": ", ".join(book.get("authors", ["Autor desconhecido"])),
                "year": book.get("publishedDate", "Ano desconhecido").split("-")[0],
                "description": book.get("description", "Sem descrição disponível."),
                "cover_url": book.get("imageLinks", {}).get("thumbnail", None)
            }

    return None