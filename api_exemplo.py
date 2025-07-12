

import requests
import json

# --- CONFIGURAÇÃO ---
# Usando a última chave de API que você forneceu.
from config import RIOT_API_KEY as API_KEY 

# Riot ID do jogador
GAME_NAME = "Czekolad"
TAG_LINE = "BAR"

# A região de roteamento para a conta. EUW, EUNE, TR, RU pertencem a 'europe'.
ROUTING_REGION = "europe"

# --- CONSTRUÇÃO DA URL ---
# Este é o endpoint para procurar contas por Riot ID
url = f"https://{ROUTING_REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}"

# --- FAZENDO A REQUISIÇÃO ---
headers = {
    "X-Riot-Token": API_KEY
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    account_data = response.json()

    # --- EXTRAINDO A INFORMAÇÃO ---
    puuid = account_data['puuid']

    print(f"SUCESSO!")
    print(f"Riot ID: {account_data['gameName']}#{account_data['tagLine']}")
    print(f"PUUID: {puuid}")
    
    with open("account_data.json", "w") as f:
        json.dump(account_data, f, indent=4)
    print("\nDados da conta salvos em 'account_data.json'")

except requests.exceptions.HTTPError as err:
    print(f"ERRO HTTP: {err}")
    print(f"Código de Status: {err.response.status_code}")
    if err.response.status_code in [401, 403]:
        print("A chave de API (API_KEY) provavelmente expirou. Por favor, gere uma nova no portal da Riot.")
    elif err.response.status_code == 404:
        print(f"Riot ID '{GAME_NAME}#{TAG_LINE}' não encontrado.")
    else:
        print(f"Conteúdo da resposta: {err.response.text}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
