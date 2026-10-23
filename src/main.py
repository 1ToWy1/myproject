import requests


def get_weather() -> None:
    url = "https://wttr.in/?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        print("Текущая погода:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка во время запроса: {e}")


if __name__ == "__main__":
    get_weather()
