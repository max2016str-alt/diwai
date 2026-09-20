import os
import requests

PERSONALITY_FILE = "personality.txt"

DEFAULT_PERSONALITY = """Ты DiwAI.

Ты дружелюбный ИИ-помощник.

Отвечай простым и понятным языком.

Если пользователь шутит — можешь немного пошутить в ответ.

Не груби пользователю.

Разработчик проекта: Diwandis.
"""

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3:4b"


def load_personality():
    if not os.path.exists(PERSONALITY_FILE):
        with open(PERSONALITY_FILE, "w", encoding="utf-8") as file:
            file.write(DEFAULT_PERSONALITY)

    with open(PERSONALITY_FILE, "r", encoding="utf-8") as file:
        return file.read()


def generate_answer(message):
    personality = load_personality()

    prompt = f"""{personality}

Пользователь: {message}

DiwAI:"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()
        return data["response"].strip()

    except Exception as e:
        return f"❌ Ошибка подключения к Ollama:\n{e}"
