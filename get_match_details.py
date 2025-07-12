import requests
import json
import time

# --- CONFIGURAÇÃO ---
from config import RIOT_API_KEY as API_KEY
ROUTING_REGION = "europe"

# --- LER O ID DA PARTIDA ---
try:
    with open("match_ids.json", "r") as f:
        match_ids = json.load(f)
        if not match_ids:
            print("ERRO: O arquivo 'match_ids.json' está vazio.")
            exit()
    # Vamos pegar o primeiro ID da lista para este exemplo
    match_id_to_fetch = match_ids[0]
    print(f"Buscando detalhes para a partida: {match_id_to_fetch}")

except FileNotFoundError:
    print("ERRO: Arquivo 'match_ids.json' não encontrado. Execute o script get_matches.py primeiro.")
    exit()

# --- CONSTRUÇÃO DA URL ---
url = f"https://{ROUTING_REGION}.api.riotgames.com/lol/match/v5/matches/{match_id_to_fetch}"

headers = {
    "X-Riot-Token": API_KEY
}

# --- FAZENDO A REQUISIÇÃO ---
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    match_data = response.json()

    # --- EXTRAINDO E EXIBINDO OS DADOS ---
    print("\n--- DADOS DA PARTIDA PARA O MODELO ---")
    
    participants = match_data['info']['participants']
    
    print("\n[bold blue]EQUIPE AZUL (Team ID: 100)[/]")
    for p in participants:
        if p['teamId'] == 100:
            print(f"  - Campeão: {p['championName']:<15} | Venceu: {p['win']}")

    print("\n[bold red]EQUIPE VERMELHA (Team ID: 200)[/]")
    for p in participants:
        if p['teamId'] == 200:
            print(f"  - Campeão: {p['championName']:<15} | Venceu: {p['win']}")

    # Salvar os dados completos da partida para análise
    with open(f"match_detail_{match_id_to_fetch}.json", "w") as f:
        json.dump(match_data, f, indent=4)
    print(f"\nDados completos da partida salvos em 'match_detail_{match_id_to_fetch}.json'")

except requests.exceptions.HTTPError as err:
    print(f"\nERRO HTTP: {err}")
    if err.response.status_code in [401, 403]:
        print("A chave de API (API_KEY) provavelmente expirou. Por favor, gere uma nova no portal da Riot.")
    else:
        print(f"Conteúdo da resposta: {err.response.text}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
