from profile import show_profile, set_name
from settings import show_settings, show_version


def run_command(command):
    if command == "/about":
        return show_version()

    elif command == "/settings":
        return show_settings()

    elif command == "/profile":
        return show_profile()

    elif command.startswith("/setname "):
        name = command[len("/setname "):].strip()
        return set_name(name)

    elif command == "/help":
        return (
            "Команды DiwAI:\n"
            "/about — версия\n"
            "/settings — настройки\n"
            "/profile — профиль\n"
            "/setname <имя> — изменить имя\n"
            "/help — помощь\n"
            "/clear — очистить историю"
        )

    else:
        return None