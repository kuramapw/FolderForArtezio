import requests


def exchange(amount: float, currency: str, target: str) -> float:
    res = requests.get("https://api.exchangerate-api.com/v4/latest/" + currency)
    content = res.json()
    return amount * content['rates'][target]


print(exchange(500, "USD", "RUB"))
