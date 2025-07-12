
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from rich import print

# Passo 1 & 2: Carregar e preparar os dados (exemplo com dados fictícios)
# Na realidade, você teria milhares de linhas de partidas reais.
# Aumentamos o dataset para evitar o erro de classe única no treino.
data = {
    'azir_blue': [1, 0, 1, 0, 1, 0, 1, 0],
    'jinx_blue': [0, 1, 0, 1, 0, 1, 0, 1],
    'garen_red': [1, 0, 0, 1, 1, 0, 1, 0],
    'lux_red':   [0, 1, 1, 0, 0, 1, 0, 1],
    'winner_is_blue':  [1, 0, 1, 0, 0, 1, 1, 0] # 1 = Azul venceu, 0 = Vermelho venceu
}
df = pd.DataFrame(data)

X = df.drop('winner_is_blue', axis=1)
y = df['winner_is_blue']

# Dividir dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Passo 3: Treinar o modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Medir a acurácia (de forma simples)
accuracy = model.score(X_test, y_test)
print(f"Acurácia do Modelo: {accuracy:.2%}")

# Passo 4: Fazer uma nova previsão
# Suponha uma nova partida: Azir no time azul, Lux no time vermelho
new_match = pd.DataFrame([{'azir_blue': 1, 'jinx_blue': 0, 'garen_red': 0, 'lux_red': 1}])
win_probabilities = model.predict_proba(new_match)[0]

prob_blue_wins = win_probabilities[1]
prob_red_wins = win_probabilities[0]

# Calcular Odds
odds_blue = 1 / prob_blue_wins
odds_red = 1 / prob_red_wins

# Passo 5: Exibir na interface (usando a biblioteca 'rich')
print("--- PREVISÃO DA PARTIDA ---")
print(f"[bold green]Acurácia:[/] {accuracy:.2%}")
print("[bold]CONFRONTO:[/] T1 vs AL")
print("[bold]PROBABILIDADES:[/]")
print(f"   (Azul) T1: [blue]{prob_blue_wins:.1%}[/]")
print(f"   (Vermelho) AL: [red]{prob_red_wins:.1%}[/]")
print("[bold yellow]ODDS:[/]")
print(f"   (Azul) AZUL -> {odds_blue:.2f}")
print(f"   (Vermelho) VERMELHO -> {odds_red:.2f}")
