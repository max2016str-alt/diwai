import json
import os

FILE_NAME = "user.json"


def load_profile():
    if not os.path.exists(FILE_NAME):
        profile = {
            "name": "",
            "preferences": []
        }
        save_profile(profile)
        return profile

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_profile(profile):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=4)


def get_name():
    profile = load_profile()
    return profile.get("name", "")


def set_name(name):
    profile = load_profile()

    profile["name"] = name.strip()

    save_profile(profile)

    return f"✅ Запомнил! Теперь твоё имя: {name}"


def show_profile():
    profile = load_profile()

    name = profile.get("name", "")

    if name == "":
        name = "Не указано"

    return (
        "👤 Профиль DiwAI\n"
        f"Имя: {name}\n"
        f"Настроек: {len(profile.get('preferences', []))}"
    )


def first_start():
    name = get_name()

    if name == "":
        print("👋 Добро пожаловать в DiwAI!")
        print()

        name = input("Как тебя зовут? ")

        set_name(name)

        print(f"\nПриятно познакомиться, {name}! 😊")

    else:
        print(f"👋 С возвращением, {name}!")