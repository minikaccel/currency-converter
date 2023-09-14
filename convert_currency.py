import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")


def convert(want: str, have: str, value: float = 1):
    """Конвертирует валюту"""
    api_url = f"https://api.api-ninjas.com/v1/convertcurrency?want={want}&have={have}&amount={value}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    if response.status_code == requests.codes.ok:
        output = response.json()
        new_amount, *b = output.values()
        return new_amount
    else:
        print("Error")


print(convert("RUB", "USD", 1))
