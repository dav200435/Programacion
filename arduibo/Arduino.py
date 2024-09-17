import requests
from bs4 import BeautifulSoup

class Arduino:
    def __init__(self):
        
        # URL de la página web
        self.url = "http://192.168.4.1"
    def conect(self):
        response = requests.get(self.url)
        
        # Verificar que la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener el contenido HTML de la página
            html_content = response.text
        
            # Analizar el contenido HTML con BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
        
            # Imprimir el contenido HTML formateado
            return soup.prettify()
        else:
            print("Error al acceder a la página:", response.status_code)