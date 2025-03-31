#Pacotes ou bibliotecas criados por terceiros. Não são modulos padrão de python.
#Request -> pip install requests==2.31.0

print("\n Importação e uso de módulos de terceiros...")
import requests

url = "https://mpe.mpmg.mp.br"
response = requests.get(url)
print(f"Solicitação HTTP para {url} Retornou o status {response.status_code} ")
