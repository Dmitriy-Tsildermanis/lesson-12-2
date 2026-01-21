from datetime import datetime
from pathlib import Path

from news import get_news
from save_to_file import save_to_file


def main() -> None:
    """Главная функция для работы приложения"""
    quere = input("Введите ключевые слова: ")
    exclude_word = input("Введите слова для фильтрации (через запятую): ").split(", ")
    today = datetime.today()
    today_string = today.strftime("%Y-%m-%d")

    print(f"Поиск статей по запросу: {quere}")
    articles_list = get_news(quere, exclude_word)

    if not articles_list:
        print("Не удалось получить статьи или список пуст")
        return

    print(f"Найдено статей: {len(articles_list)}")

    file_name = f'{today_string}_{quere.replace(" ", "_")}.json'

    base_dir = Path(__file__).parent.parent
    file_path = base_dir / "data" / file_name

    print(f"Сохранение в файл: {file_path}")
    save_to_file(articles_list, str(file_path))


if __name__ == "__main__":
    main()
