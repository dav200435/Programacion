import requests
class controler:
    def __init__(self,ip) -> None:
        self.ip = "http://"+ip
    def Power(self):
        url = self.ip
        params = {
        'm': '1',
        'o': '1'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print('Solicitud exitosa:', response.text)
        else:
            print('Error:', response.status_code)
    def action(self):
        self.Power()
