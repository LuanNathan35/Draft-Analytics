# LoL Pro-Match Predictor

## Visão Geral
Este projeto é uma ferramenta de análise de dados que utiliza Machine Learning para prever a probabilidade de vitória em partidas de League of Legends de alto elo e profissionais, com base na composição das equipes (draft).

O objetivo é fornecer insights estatísticos para a comunidade, analistas e fãs de e-sports, ajudando a entender a profundidade estratégica da fase de seleção de campeões.

## Como Funciona
O sistema opera em um pipeline de três estágios:
1.  **Coleta de Dados:** Um conjunto de scripts coleta dados de partidas de alta qualidade (Challenger/Grandmaster) usando a API oficial da Riot Games.
2.  **Treinamento do Modelo:** Os dados coletados são processados e usados para treinar um modelo de classificação que aprende os padrões de vitória associados a diferentes composições.
3.  **Previsão:** O modelo treinado é usado para calcular a probabilidade de vitória para novas partidas.

## Instalação
1.  **Clone este repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```
2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure sua API Key:**
    *   Renomeie o arquivo `config_example.py` para `config.py`.
    *   Abra `config.py` e insira sua chave da API da Riot.

## Como Usar
1.  **Coleta de Dados:** Execute os scripts de coleta na ordem para construir seu dataset.
    ```bash
    python get_matches.py
    python get_match_details.py
    ```
2.  **Fazer uma Previsão:** Execute o script principal para ver uma previsão de exemplo.
    ```bash
    python lol_predictor.py
    ```

## Aviso Legal
Este projeto foi criado para fins educacionais e de estudo, em conformidade com as políticas de desenvolvimento da Riot Games. Ele não é afiliado ou endossado pela Riot Games.
