import requests
import json

# --- CONFIGURAÇÃO ---
# Usando a mesma chave de API. Se der erro, precisaremos de uma nova.
from config import RIOT_API_KEY as API_KEY

# O PUUID que encontramos no script anterior
PUUID = "IK0jbrRRuwzShvOSXcu10cGWa7IM8Haav4BQBV33huPRZBC01tMkTyRB2ta6tzAKF0O-vT95w3Pi-Q"

# A região de roteamento para partidas (EUW -> europe)
ROUTING_REGION = "europe"

# --- CONSTRUÇÃO DA URL ---
# Endpoint para buscar a lista de IDs de partidas por PUUID
url = f"https://{ROUTING_REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids"

# Parâmetros adicionais: vamos pegar as últimas 20 partidas
params = {
    "count": 20
}

# --- FAZENDO A REQUISIÇÃO ---
headers = {
    "X-Riot-Token": API_KEY
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    match_ids = response.json()

    # --- EXIBINDO O RESULTADO ---
    print(f"SUCESSO! Encontradas {len(match_ids)} partidas.")
    print("Lista de Match IDs:")
    for match_id in match_ids:
        print(f"  - {match_id}")

    with open("match_ids.json", "w") as f:
        json.dump(match_ids, f, indent=4)
    print("\nLista de IDs salva em 'match_ids.json'")

except requests.exceptions.HTTPError as err:
    print(f"ERRO HTTP: {err}")
    if err.response.status_code in [401, 403]:
        print("A chave de API (API_KEY) provavelmente expirou. Por favor, gere uma nova no portal da Riot.")
    else:
        print(f"Conteúdo da resposta: {err.response.text}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
