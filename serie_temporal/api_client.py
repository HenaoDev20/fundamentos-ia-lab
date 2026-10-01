import requests

def obtener_datos_api():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365&interval=daily"
    print("Conectando a la API de CoinGecko...")
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()['prices']