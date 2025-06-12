import requests

url = "http://localhost:8090/api/main/focus"

payload = {
    "target":"Mars",
    "mode": "equatorial"  # или "equatorial", ако подавате координати
}



response = requests.post(url, payload)


if response.status_code == 200:
    print("Успешно центрирано върху обекта.")
else:
    print("Грешка:", response.status_code, response.text)