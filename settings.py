from config import APP_NAME, VERSION


def show_settings():
    return (
        f"⚙️ Настройки {APP_NAME}\n"
        f"Версия: {VERSION}\n"
        "Режим: разработка\n"
        "Память: включена\n"
    )


def show_version():
    return f"{APP_NAME} v{VERSION}"