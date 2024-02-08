import requests

class Horoscope:
    def __init__(self, date, horoscope_data):
        self.date = date
        self.horoscope_data = horoscope_data

class HoroscopeResponse:
    def __init__(self, data, status, success):
        self.data = Horoscope(data['date'], data['horoscope_data'])
        self.status = status
        self.success = success

response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
if response.status_code == 200:
    response_data = response.json()
    horoscope_response = HoroscopeResponse(**response_data)

    print(horoscope_response.data.date)
    print(" ")
    print(horoscope_response.data.horoscope_data)
    print(" ")
    print(horoscope_response.status)
    print(" ")
    print(horoscope_response.success)
else:
    print("Failed to fetch horoscope. Status code:", response.status_code)