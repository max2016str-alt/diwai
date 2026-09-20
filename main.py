from memory import load_history, save_history
from config import APP_NAME, VERSION, BUILD, DEVELOPER
from ai import generate_answer
from commands import run_command
from profile import first_start


print("====================")
print(f"       {APP_NAME}")
print(f"   v{VERSION} Build {BUILD}")
print("====================")
print()
print(f"Разработчик: {DEVELOPER}")
print()

# Проверка профиля
first_start()

history = load_history()


def reply(message):
    command = run_command(message)

    if command:
        return command

    elif message == "/clear":
        history.clear()
        save_history(history)
        return "История очищена."

    else:
        return generate_answer(message)


print()
print("Введите /help, чтобы увидеть список команд.")
print()

try:
    while True:
        user = input("Ты: ")

        if user.lower() in ["выход", "/exit"]:
            print("DiwAI: До встречи! 👋")
            break

        answer = reply(user)

        print("DiwAI:", answer)

        history.append({
            "user": user,
            "ai": answer
        })

        save_history(history)

except KeyboardInterrupt:
    print("\nDiwAI: Работа завершена.")