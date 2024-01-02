from requests import get
from time import sleep
from datetime import datetime


def current_time() -> str:
    """
    Returns the current time in the format '%d.%m.%Y %H:%M:%S'.

    Returns:
        str: The current time in the format '%d.%m.%Y %H:%M:%S'.
    """
    dt = datetime.now()
    dt = dt.strftime('%d.%m.%Y %H:%M:%S')
    return dt
def log(text: str) -> None:
    """
    Logs a message to the console with the current time.

    Args:
        text (str): The message to be logged.
    """
    print(f"[{current_time()}] {text}")


id = input("Введите ваш ID с бота, его можно получить в @getmyid_bot: ")
wait = input("Введите время ожидания в секундах: ")

url = f"https://advert-app.com/seenAd/{id}"




while True:
    log(f"Жду {wait} секунд")
    sleep(int(wait))

    log("Начинаю крутить просмотр...")
    try:
        response = get(url)
        json = response.json()
        status = json['status']
    except:
        status = "error"


    if status == "ok":
        log("Просмотр завершен")
    else:
        log("Что-то пошло не так")