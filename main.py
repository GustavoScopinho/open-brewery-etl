import requests

url  = 'https://api.openbrewerydb.org/breweries'

all_breweries = []
page = 1
per_page = 50

while True:
    response = requests.get(url, params={'page': page, 'per_page': per_page})
    if response.status_code != 200:
        print(f'Erro na requisição: {response.status_code}')
        break

    data = response.json()
    if not data:
        break

    all_breweries.extend(data)
    print(f"Página {page} carregada com {len(data)} registros.")
    page += 1
    

print(f"Total de registros coletados: {len(all_breweries)}")


print(type(all_breweries))