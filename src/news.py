import os

import requests
from dotenv import load_dotenv

# from datetime import datetime


load_dotenv()


def get_news(query: str, exclude_words: list) -> list:
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    # today = datetime.today()

    if not api_key or not base_url:
        print("Ошибка: не найдены API_KEY или BASE_URL в переменных окружения")
        return []

    params = {
        "q": query,
        # 'from': today.strftime('%Y-%m-%d'),
        "sortBy": "",
        "apiKey": api_key,
    }
    try:
        response = requests.get(url=base_url, params=params)

        news_data = response.json()
        if news_data.get("status") != "ok":
            return []

        articles_list = news_data.get("articles", [])
        articles_result = []

        for article in articles_list:
            content = f'{article.get("title")} {article.get("content")}'.lower()

            # продвинутый способ:
            if any(word.lower() in content for word in exclude_words):
                continue

            # простой способ:
            # exclude_flag = False
            # for word in exclude_words:
            #     if word in content:
            #         exclude_flag = True
            # if exclude_flag:
            #     continue

            articles_result.append(
                {
                    "title": article.get("title"),
                    "author": article.get("author"),
                    "description": article.get("content"),
                    "url": article.get("url"),
                }
            )

        return articles_result
    except requests.RequestException:
        return []
    except Exception:
        return []
