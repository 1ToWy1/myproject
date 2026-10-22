import requests


def get_weather():
    url = "https://wttr.in/?format=3"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print("Текущая погода:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")


if __name__ == "__main__":
    get_weather()
