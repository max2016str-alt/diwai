import json
import os

FILE_NAME = "history.json"


def load_history():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)