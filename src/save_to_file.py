import json


def save_to_file(data: list, file_path: str) -> None:
    """Сохранение данных по указанному пути"""
    try:
        with open(file_path, "w", encoding="utf-8") as data_file:
            json.dump(data, data_file)
    except Exception:
        pass
